// ============================================================================
// Pokemon Codenames – app.js
// Shared Supabase setup, auth, realtime, and logic for all three screens
// (landing / lobby / game). Plain JS, no build step – runs in the browser.
// ============================================================================

const SUPABASE_URL = "https://fjhijkszcugwxtmlbudz.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZqaGlqa3N6Y3Vnd3h0bWxidWR6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODMwMTExODcsImV4cCI6MjA5ODU4NzE4N30.MY29L3dGhgCAyrKS0bx0E30DbwiYHrb75dIzmjKBRZI";

const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const SESSIONS_KEY = "pc_sessions"; // map of roomId → session
const POLL_MS = 2500; // background self-heal poll interval

// Reliable CDN for Pokemon artwork (jsDelivr mirror of the PokeAPI sprites).
const ART_BASE = "https://cdn.jsdelivr.net/gh/PokeAPI/sprites@master/sprites/pokemon/other/official-artwork";
const SPRITE_BASE = "https://cdn.jsdelivr.net/gh/PokeAPI/sprites@master/sprites/pokemon";

// ----------------------------------------------------------------------------
// App state
// ----------------------------------------------------------------------------
const state = {
  user: null,
  nickname: "",
  roomId: null,
  playerId: null,
  room: null,
  players: [],
  cards: [],
  cardKey: null, // map position -> colour, only populated for clue givers
  channel: null,
  me: null, // players row for the current user
  turnStartRevealed: new Set(), // positions already revealed when this turn's clue arrived
  lastClueWord: null, // tracks clue identity so we snapshot exactly once per clue
  revealedSnapshot: null, // Set of revealed positions from the last render (for reveal animation + sounds)
  _prevClueCount: null, // last seen clue_count (to detect new clues → sound)
  _prevStatus: null, // last seen room.status (to detect game-over → sound)
};

let lastSignature = null;   // used by the poll to avoid needless re-renders
let statsRequested = false; // record the two-player result only once
let serverOffsetMs = 0;     // (server clock) - (this device's clock)
let aiTurnTimer = null;     // pending "AI is thinking" timeout (vs-AI mode)

// Measure the gap between the Supabase server clock and this device's clock so
// every device shows the same elapsed time no matter how wrong its own clock is.
async function syncServerClock() {
  try {
    const { data, error } = await sb.rpc("server_now");
    if (error) throw error;
    serverOffsetMs = new Date(data).getTime() - Date.now();
  } catch (err) {
    serverOffsetMs = 0;
  }
}

function serverNow() {
  return Date.now() + serverOffsetMs;
}

// ----------------------------------------------------------------------------
// Small DOM helpers
// ----------------------------------------------------------------------------
const $ = (sel, root = document) => root.querySelector(sel);
const $all = (sel, root = document) => Array.from(root.querySelectorAll(sel));

function showScreen(name) {
  $all(".screen").forEach((el) => el.classList.remove("active"));
  $(`#screen-${name}`).classList.add("active");
}

function toast(message) {
  const stack = $("#toast-stack");
  const el = document.createElement("div");
  el.className = "toast";
  el.textContent = message;
  stack.appendChild(el);
  setTimeout(() => el.remove(), 4200);
}

function setRoomPill(code) {
  const pill = $("#room-pill");
  const refresh = $("#refresh-btn");
  if (code) {
    $("#room-pill-code").textContent = code;
    pill.classList.remove("hidden");
    refresh.classList.remove("hidden");
  } else {
    pill.classList.add("hidden");
    refresh.classList.add("hidden");
  }
}

// ----------------------------------------------------------------------------
// Sound effects – synthesized with the Web Audio API (no asset files needed,
// works offline). Controlled by a header toggle, preference saved locally.
// ----------------------------------------------------------------------------
let audioCtx = null;
let soundOn = localStorage.getItem("pc_sound") !== "off"; // default on

function ensureAudio() {
  if (!audioCtx) {
    try { audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch { audioCtx = null; }
  }
  return audioCtx;
}

function _tone(freq, dur, type = "sine", gain = 0.15, when = 0) {
  const ctx = ensureAudio();
  if (!ctx) return;
  const t = ctx.currentTime + when;
  const osc = ctx.createOscillator();
  const g = ctx.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, t);
  g.gain.setValueAtTime(0.0001, t);
  g.gain.exponentialRampToValueAtTime(gain, t + 0.012);
  g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  osc.connect(g);
  g.connect(ctx.destination);
  osc.start(t);
  osc.stop(t + dur + 0.03);
}

function playSound(name) {
  if (!soundOn) return;
  const ctx = ensureAudio();
  if (!ctx) return;
  if (ctx.state === "suspended") ctx.resume();
  switch (name) {
    case "clue":    _tone(523, 0.12, "triangle", 0.12); _tone(784, 0.13, "triangle", 0.12, 0.1); break;
    case "correct": _tone(659, 0.1, "sine", 0.17); _tone(988, 0.15, "sine", 0.17, 0.09); break;
    case "wrong":   _tone(311, 0.24, "sawtooth", 0.12); break;
    case "assassin":_tone(196, 0.5, "sawtooth", 0.18); _tone(147, 0.6, "sawtooth", 0.15, 0.08); break;
    case "ai":      _tone(440, 0.09, "square", 0.07); _tone(370, 0.12, "square", 0.07, 0.08); break;
    case "win":     [523, 659, 784, 1047].forEach((f, i) => _tone(f, 0.17, "triangle", 0.16, i * 0.12)); break;
    case "lose":    [392, 330, 262].forEach((f, i) => _tone(f, 0.22, "sawtooth", 0.14, i * 0.14)); break;
  }
}

function updateSoundToggle() {
  const btn = $("#sound-toggle");
  if (!btn) return;
  btn.textContent = soundOn ? "🔊" : "🔇";
  btn.classList.toggle("sound-off", !soundOn);
}

function initSoundToggle() {
  updateSoundToggle();
  $("#sound-toggle").addEventListener("click", () => {
    soundOn = !soundOn;
    localStorage.setItem("pc_sound", soundOn ? "on" : "off");
    updateSoundToggle();
    if (soundOn) playSound("clue"); // little confirmation blip
  });
}

// ----------------------------------------------------------------------------
// Win-overlay dismissal – remember when a player chose "See the board" so the
// overlay doesn't pop back up when they switch tabs / apps and return.
// ----------------------------------------------------------------------------
const WIN_DISMISS_KEY = "pc_win_dismissed";
function _loadDismissed() {
  try { return new Set(JSON.parse(localStorage.getItem(WIN_DISMISS_KEY) || "[]")); } catch { return new Set(); }
}
function dismissWin(roomId) {
  if (!roomId) return;
  const s = _loadDismissed();
  s.add(roomId);
  localStorage.setItem(WIN_DISMISS_KEY, JSON.stringify([...s]));
}
function isWinDismissed(roomId) {
  return !!roomId && _loadDismissed().has(roomId);
}

// ----------------------------------------------------------------------------
// Local persistence – multi-room session map so users can juggle several games
// ----------------------------------------------------------------------------
function _loadSessionMap() {
  try { return JSON.parse(localStorage.getItem(SESSIONS_KEY) || "{}"); } catch { return {}; }
}

function saveSession() {
  if (!state.roomId) return;
  const map = _loadSessionMap();
  map[state.roomId] = {
    roomId: state.roomId,
    playerId: state.playerId,
    nickname: state.nickname,
    code: state.room?.code || map[state.roomId]?.code || null,
    lastVisited: Date.now(),
  };
  localStorage.setItem(SESSIONS_KEY, JSON.stringify(map));
}

function _removeSession(roomId) {
  const map = _loadSessionMap();
  delete map[roomId];
  localStorage.setItem(SESSIONS_KEY, JSON.stringify(map));
}

function _findSessionForCode(code) {
  if (!code) return null;
  const upper = code.toUpperCase();
  return Object.values(_loadSessionMap()).find((s) => s.code === upper) || null;
}

function _findLastSession() {
  const sessions = Object.values(_loadSessionMap());
  if (!sessions.length) return null;
  return sessions.sort((a, b) => (b.lastVisited || 0) - (a.lastVisited || 0))[0];
}

function _migrateOldSession() {
  const old = localStorage.getItem("pc_session");
  if (!old) return;
  try {
    const parsed = JSON.parse(old);
    if (parsed?.roomId) {
      const map = _loadSessionMap();
      map[parsed.roomId] = { ...parsed, lastVisited: Date.now() };
      localStorage.setItem(SESSIONS_KEY, JSON.stringify(map));
    }
  } catch {}
  localStorage.removeItem("pc_session");
}

function clearSession() {
  if (state.roomId) _removeSession(state.roomId);
  state.roomId = null;
  state.playerId = null;
  state.room = null;
  state.players = [];
  state.cards = [];
  state.cardKey = null;
  state.me = null;
  state.turnStartRevealed = new Set();
  state.lastClueWord = null;
  state.revealedSnapshot = null;
  state._prevClueCount = null;
  state._prevStatus = null;
  state._prevClue = null;
  lastSignature = null;
  statsRequested = false;
  if (state.channel) {
    sb.removeChannel(state.channel);
    state.channel = null;
  }
  setRoomPill(null);
  const overlay = document.getElementById("win-overlay");
  if (overlay) overlay.classList.add("hidden");
}

// ----------------------------------------------------------------------------
// Auth – anonymous sign-in, persisted by supabase-js itself
// ----------------------------------------------------------------------------
async function ensureAuth() {
  const { data } = await sb.auth.getSession();
  if (data.session) {
    state.user = data.session.user;
    return;
  }
  const { data: signInData, error } = await sb.auth.signInAnonymously();
  if (error) {
    console.error(error);
    toast("Couldn't start a session. Try reloading the page.");
    throw error;
  }
  state.user = signInData.user;
}

// Push the current auth token onto the realtime socket. Essential: our tables
// use row-level security scoped to authenticated users, so without the token
// live database-change events get filtered out and never arrive.
async function syncRealtimeAuth() {
  const { data } = await sb.auth.getSession();
  if (data.session?.access_token) {
    sb.realtime.setAuth(data.session.access_token);
  }
}

// ============================================================================
// LANDING SCREEN
// ============================================================================

function initLandingScreen() {
  $all('input[name="mode"]').forEach((input) => {
    input.addEventListener("change", () => {
      $all(".radio-chip[data-role='mode']").forEach((chip) =>
        chip.classList.toggle("checked", chip.querySelector("input").checked)
      );
      const vsAi = $('input[name="mode"]:checked')?.value === "two_player_ai";
      $("#ai-difficulty-field").classList.toggle("hidden", !vsAi);
    });
  });

  $all('input[name="ai_difficulty"]').forEach((input) => {
    input.addEventListener("change", () => {
      $all(".radio-chip[data-role='difficulty']").forEach((chip) =>
        chip.classList.toggle("checked", chip.querySelector("input").checked)
      );
    });
  });

  $all(".gen-chip input").forEach((input) => {
    input.addEventListener("change", () => {
      input.closest(".gen-chip").classList.toggle("checked", input.checked);
    });
  });

  $("#create-room-form").addEventListener("submit", handleCreateRoom);
  $("#join-room-form").addEventListener("submit", handleJoinRoom);

  const params = new URLSearchParams(window.location.search);
  const codeParam = params.get("code");
  if (codeParam) $("#join-code").value = codeParam.toUpperCase();

  // Quick-join modal
  $("#quick-join-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const errEl = $("#quick-join-error");
    errEl.textContent = "";
    const nickname = $("#quick-join-nickname").value.trim();
    if (!nickname) return;
    const code = $("#quick-join-code").dataset.code;
    const btn = e.submitter;
    btn.disabled = true;
    try {
      await ensureAuth();
      const { data, error } = await sb.rpc("join_room", { p_code: code, p_nickname: nickname });
      if (error) throw error;
      const row = data[0];
      state.nickname = nickname;
      state.roomId = row.room_id;
      state.playerId = row.player_id;
      saveSession();
      $("#quick-join-overlay").classList.add("hidden");
      await enterRoom();
    } catch (err) {
      console.error(err);
      errEl.textContent = err.message || "Couldn't join – check the link and try again.";
    } finally {
      btn.disabled = false;
    }
  });
}

function collectSettings() {
  const generations = $all('.gen-chip input:checked').map((i) => Number(i.value));
  return {
    generations: generations.length ? generations : [1],
    well_known_only: $("#well-known-toggle").checked,
    show_images: $("#show-images-toggle").checked,
    ai_difficulty: $('input[name="ai_difficulty"]:checked')?.value || "easy",
  };
}

async function handleCreateRoom(e) {
  e.preventDefault();
  const errEl = $("#create-error");
  errEl.textContent = "";
  const nickname = $("#create-nickname").value.trim();
  if (!nickname) {
    errEl.textContent = "Enter a nickname first.";
    return;
  }
  const mode = $('input[name="mode"]:checked').value;
  const settings = collectSettings();

  const btn = $("#create-room-btn");
  btn.disabled = true;
  try {
    await ensureAuth();
    const { data, error } = await sb.rpc("create_room", {
      p_nickname: nickname,
      p_mode: mode,
      p_settings: settings,
    });
    if (error) throw error;
    const row = data[0];
    state.nickname = nickname;
    state.roomId = row.room_id;
    state.playerId = row.player_id;
    saveSession();
    await enterRoom();
  } catch (err) {
    console.error(err);
    errEl.textContent = err.message || "Couldn't create the room.";
  } finally {
    btn.disabled = false;
  }
}

async function handleJoinRoom(e) {
  e.preventDefault();
  const errEl = $("#join-error");
  errEl.textContent = "";
  const nickname = $("#join-nickname").value.trim();
  const code = $("#join-code").value.trim().toUpperCase();
  if (!nickname || !code) {
    errEl.textContent = "Enter a nickname and room code.";
    return;
  }

  const btn = $("#join-room-btn");
  btn.disabled = true;
  try {
    await ensureAuth();
    const { data, error } = await sb.rpc("join_room", { p_code: code, p_nickname: nickname });
    if (error) throw error;
    const row = data[0];
    state.nickname = nickname;
    state.roomId = row.room_id;
    state.playerId = row.player_id;
    saveSession();
    await enterRoom();
  } catch (err) {
    console.error(err);
    errEl.textContent = err.message || "Couldn't join that room.";
  } finally {
    btn.disabled = false;
  }
}

// ============================================================================
// SHARED: fetching + realtime + routing between lobby/game
// ============================================================================

async function fetchRoom() {
  const { data, error } = await sb.from("rooms").select("*").eq("id", state.roomId).single();
  if (error) throw error;
  state.room = data;
}

async function fetchPlayers() {
  const { data, error } = await sb.from("players").select("*").eq("room_id", state.roomId);
  if (error) throw error;
  state.players = data || [];
  state.me = state.players.find((p) => p.id === state.playerId) || null;
}

async function fetchCards() {
  const { data, error } = await sb
    .from("cards")
    .select("*")
    .eq("room_id", state.roomId)
    .order("position", { ascending: true });
  if (error) throw error;
  state.cards = data || [];
}

async function fetchCardKeyIfSpymaster() {
  const isSpymaster = state.me?.role === "spymaster";
  const isFinished = state.room?.status === "finished";
  if (!isSpymaster && !isFinished) { state.cardKey = null; return; }
  const { data, error } = await sb.from("card_key").select("*").eq("room_id", state.roomId);
  if (error) { state.cardKey = null; return; }
  const map = {};
  (data || []).forEach((row) => (map[row.position] = row.colour));
  state.cardKey = map;
}

// A cheap fingerprint of everything that affects the display.
function computeStateSignature() {
  const r = state.room;
  const roomSig = r
    ? [
        r.status, r.mode, r.current_team, r.winner, r.guesses_remaining,
        r.clue_count, r.remaining_red, r.remaining_blue, JSON.stringify(r.current_clue),
        Array.isArray(r.clue_log) ? r.clue_log.length : 0,
        Array.isArray(r.guess_log) ? r.guess_log.length : 0,
      ].join("|")
    : "no-room";
  const playersSig = state.players
    .map((p) => `${p.id}:${p.team}:${p.role}:${p.nickname}`)
    .sort()
    .join(",");
  const cardsSig = state.cards
    .map((c) => `${c.position}:${c.revealed ? 1 : 0}:${c.revealed_colour || ""}`)
    .join(",");
  const keySig = state.cardKey ? "K" : "-";
  return [roomSig, playersSig, cardsSig, keySig].join("#");
}

let reconnectTimer = null;

function subscribeToRoom() {
  if (state.channel) {
    sb.removeChannel(state.channel);
    state.channel = null;
  }
  state.channel = sb
    .channel(`room-${state.roomId}`)
    .on(
      "postgres_changes",
      { event: "*", schema: "public", table: "rooms", filter: `id=eq.${state.roomId}` },
      async () => {
        await fetchRoom();
        await fetchCardKeyIfSpymaster();
        await render();
      }
    )
    .on(
      "postgres_changes",
      { event: "*", schema: "public", table: "players", filter: `room_id=eq.${state.roomId}` },
      async () => {
        await fetchPlayers();
        await fetchCardKeyIfSpymaster();
        await render();
      }
    )
    .on(
      "postgres_changes",
      { event: "*", schema: "public", table: "cards", filter: `room_id=eq.${state.roomId}` },
      async (payload) => {
        await fetchCards();
        await render(payload.new ? payload.new.position : null);
      }
    )
    .subscribe((status) => {
      if (status === "SUBSCRIBED") {
        if (reconnectTimer) {
          clearTimeout(reconnectTimer);
          reconnectTimer = null;
        }
        resyncRoom();
      } else if (status === "CHANNEL_ERROR" || status === "TIMED_OUT" || status === "CLOSED") {
        if (!reconnectTimer && state.roomId) {
          reconnectTimer = setTimeout(() => {
            reconnectTimer = null;
            subscribeToRoom();
          }, 2000);
        }
      }
    });
}

// Re-fetch everything and re-render. Used after our own actions (instant local
// feedback), on reconnect, on tab focus, and by the manual refresh.
async function resyncRoom(changedPosition) {
  if (!state.roomId) return;
  try {
    await fetchRoom();
    await fetchPlayers();
    await fetchCards();
    await fetchCardKeyIfSpymaster();
    await render(changedPosition);
  } catch (err) {
    console.error("Resync failed:", err);
  }
}

// Background safety net: every couple of seconds, quietly pull state and
// re-render only if something changed.
async function pollTick() {
  if (!state.roomId || document.hidden) return;
  try {
    await fetchRoom();
    await fetchPlayers();
    await fetchCards();
    await fetchCardKeyIfSpymaster();
    if (computeStateSignature() !== lastSignature) await render();
  } catch (err) {
    /* transient – next tick retries */
  }
}

async function enterRoom() {
  await fetchRoom();
  saveSession(); // update code in session map now that room is loaded
  await fetchPlayers();
  if (!state.me) {
    clearSession();
    showScreen("landing");
    return;
  }
  await fetchCards();
  await fetchCardKeyIfSpymaster();
  subscribeToRoom();
  setRoomPill(state.room.code);
  await render();
  if (isObserver()) {
    toast("All seats are taken – you've joined as an observer.");
  }
}

// ----------------------------------------------------------------------------
// Rendering – single entry point that routes to lobby or game
// ----------------------------------------------------------------------------
async function render(changedPosition) {
  if (!state.room) return;
  if (state.room.status !== "lobby" && state.cards.length === 0) {
    await fetchCards();
    await fetchCardKeyIfSpymaster();
  }
  renderInner(changedPosition);
  lastSignature = computeStateSignature();
}

function renderInner(changedPosition) {
  const room = state.room;
  if (!room) return;
  setRoomPill(room.code);

  if (room.status === "lobby") {
    renderLobby();
    showScreen("lobby");
    return;
  }
  renderGame(changedPosition);
  showScreen("game");
}

// ----------------------------------------------------------------------------
// Board rendering (shared by the lobby preview and the game)
// ----------------------------------------------------------------------------
function makeTile(card, { interactive, animatePositions }) {
  const tile = document.createElement("div");
  tile.className = "tile";
  const revealed = card.revealed;
  const peekColour = !revealed && state.cardKey ? state.cardKey[card.position] : null;

  if (revealed) {
    tile.classList.add("revealed");
    tile.dataset.colour = card.revealed_colour;
  } else if (peekColour) {
    tile.dataset.peek = peekColour;
  }

  const allowClick = interactive && canReveal() && !revealed;
  if (!revealed && !allowClick) tile.classList.add("locked");
  // Scan-sweep animation for newly revealed tiles. When several reveal at once
  // (e.g. the AI's turn) stagger them so they colour in one after another.
  const animIdx = animatePositions ? animatePositions.indexOf(card.position) : -1;
  if (revealed && animIdx >= 0) {
    tile.classList.add("scan-sweep");
    if (animIdx > 0) tile.style.setProperty("--sweep-delay", `${animIdx * 0.22}s`);
  }

  const peekLabel = { red: "R", blue: "B", neutral: "N", assassin: "A" };
  const badgeHtml = peekColour ? `<div class="peek-badge">${peekLabel[peekColour]}</div>` : "";

  // Reliable artwork via jsDelivr, with a fallback to the smaller default
  // sprite if the artwork PNG is ever missing, so tiles never stay blank.
  const artUrl = `${ART_BASE}/${card.pokemon_id}.png`;
  const fallbackUrl = `${SPRITE_BASE}/${card.pokemon_id}.png`;

  tile.innerHTML = `
    ${badgeHtml}
    <div class="tile-img-wrap"><img src="${artUrl}" alt="${escapeHtml(card.name)}" decoding="async" onerror="this.onerror=null;this.src='${fallbackUrl}'" /></div>
    <div class="tile-name">${escapeHtml(card.name)}</div>
  `;

  if (allowClick) tile.addEventListener("click", () => handleRevealCard(card.position));
  return tile;
}

function renderBoardInto(el, opts) {
  const showImages = state.room?.settings?.show_images !== false;
  const clickable = opts.interactive && canReveal();
  const sig =
    state.cards
      .map((c) => {
        const peek = !c.revealed && state.cardKey ? state.cardKey[c.position] : "";
        return `${c.position}:${c.pokemon_id}:${c.revealed ? c.revealed_colour : "?"}:${peek}`;
      })
      .join(",") + `|${showImages ? "img" : "noimg"}|${clickable ? "click" : "lock"}`;

  // If nothing that affects the board has changed, leave the existing tiles
  // (and their already-loaded images) untouched instead of rebuilding.
  // Exception: always rebuild when there are tiles to animate so the
  // scan-sweep plays on each newly revealed tile.
  const hasAnim = opts.animatePositions && opts.animatePositions.length > 0;
  if (el.dataset.sig === sig && !hasAnim) return;
  el.dataset.sig = sig;

  el.innerHTML = "";
  el.classList.toggle("no-images", !showImages);
  state.cards.forEach((card) => el.appendChild(makeTile(card, opts)));
}

// ============================================================================
// LOBBY SCREEN
// ============================================================================

function initLobbyScreen() {
  $("#leave-room-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });

  $("#copy-code-btn").addEventListener("click", async () => {
    const code = state.room?.code;
    if (!code) return;
    const url = `${window.location.origin}${window.location.pathname}?code=${code}`;
    try {
      await navigator.clipboard.writeText(url);
      toast("Invite link copied.");
    } catch {
      toast(`Room code: ${code}`);
    }
  });

  $("#start-game-btn").addEventListener("click", handleStartGame);
}

function seatButtonsHtml(team) {
  return `
    <div class="seat-btns">
      <button class="btn btn-ghost" data-action="claim" data-team="${team}" data-role="operative">Join as clue receiver</button>
      <button class="btn btn-ghost" data-action="claim" data-team="${team}" data-role="spymaster">Be clue giver</button>
    </div>`;
}

function renderTeamColumn(team) {
  const col = $(`#team-${team}-list`);
  const teamPlayers = state.players.filter((p) => p.team === team);
  const spymaster = teamPlayers.find((p) => p.role === "spymaster");
  const operatives = teamPlayers.filter((p) => p.role === "operative");

  let html = `<div class="role-slot">Clue giver</div>`;
  html += spymaster ? playerChipHtml(spymaster) : `<div class="empty-slot">Open seat</div>`;

  html += `<div class="role-slot">Clue receivers</div>`;
  html += operatives.length
    ? operatives.map(playerChipHtml).join("")
    : `<div class="empty-slot">No clue receivers yet</div>`;

  col.innerHTML = html;
}

function playerChipHtml(p) {
  const canRemove =
    state.me && state.me.is_host && state.room && state.room.status === "lobby" && p.team;
  const removeBtn = canRemove
    ? `<button class="remove-seat" data-remove="${p.id}" title="Remove from role">×</button>`
    : "";
  return `<div class="player-chip"><span>${escapeHtml(p.nickname)}</span><span class="chip-right">${
    p.is_host ? `<span class="host-badge">HOST</span>` : ""
  }${removeBtn}</span></div>`;
}

function renderLobby() {
  if (!state.room) return;
  const room = state.room;
  const is2p = isTwoPlayer(room);
  const isAi = isVsAI(room);
  const coop = is2p || isAi; // humans share the blue side, pick giver/receiver
  $("#lobby-room-code").textContent = room.code;

  // Mode instructions
  const info = $("#lobby-info");
  if (room.mode === "in_person") {
    info.classList.remove("hidden");
    info.innerHTML = `<strong>In-person mode.</strong> Share this screen so everyone can see the board. Each clue giver should join separately on their own phone using the room code, so they can privately see which Pokémon belong to their team. Everyone else can watch and call out guesses from this shared screen.`;
  } else if (isAi) {
    info.classList.remove("hidden");
    info.innerHTML = `<strong>Two-player vs AI (${escapeHtml(room.settings?.ai_difficulty || "easy")}).</strong> You're the blue team – one clue giver, one clue receiver. Claim clue giver to begin. After each of your turns the AI reveals some of its own red tiles, so race to clear all your blue Pokémon first – and never touch the assassin.`;
  } else if (is2p) {
    info.classList.remove("hidden");
    const modeLabel = isAsyncMode(room) ? "Turn-by-turn mode" : "Two-player mode";
    info.innerHTML = `<strong>${modeLabel}.</strong> One of you is the clue giver, the other the clue receiver. Claim clue giver to begin. Work together to reveal all of your team's Pokémon in as few rounds as possible – and never touch the assassin.`;
  } else {
    info.classList.add("hidden");
  }

  // Board preview (no colours unless you've claimed clue giver)
  renderBoardInto($("#lobby-board"), { interactive: false });

  // Team columns
  const redCol = $("#lobby-red-col");
  const blueCol = $("#lobby-blue-col");
  if (coop) {
    redCol.classList.add("hidden");
    blueCol.classList.remove("hidden");
    $("#lobby-blue-title").textContent = isAi ? "Your team (vs AI)" : "Players";
    renderTeamColumn("blue");
  } else {
    redCol.classList.remove("hidden");
    blueCol.classList.remove("hidden");
    $("#lobby-red-title").textContent = "Red team";
    $("#lobby-blue-title").textContent = "Blue team";
    renderTeamColumn("red");
    renderTeamColumn("blue");
  }

  // Seat picker
  const seatArea = $("#seat-picker");
  if (state.me && state.me.team) {
    const roleLabel = state.me.role === "spymaster" ? "clue giver" : "clue receiver";
    const teamLabel = coop ? "" : ` on <strong>${state.me.team}</strong>`;
    const waitNote = (coop && state.me.role === "operative")
      ? `You're set as <strong>clue receiver</strong>. Waiting for the clue giver to start and send the first clue.`
      : `You're set as <strong>${roleLabel}</strong>${teamLabel}. ${coop ? "" : "Waiting for the host to start."}`;
    seatArea.className = "";
    seatArea.innerHTML = `<div class="waiting-note">${waitNote}</div>`;
  } else if (coop) {
    seatArea.className = "";
    seatArea.innerHTML = `
      <div class="team-col">
        <div class="seat-btns">
          <button class="btn btn-ghost" data-action="claim" data-team="blue" data-role="spymaster">Be clue giver</button>
          <button class="btn btn-ghost" data-action="claim" data-team="blue" data-role="operative">Be clue receiver</button>
        </div>
      </div>`;
  } else {
    seatArea.className = "teams-grid";
    seatArea.innerHTML = `
      <div class="team-col team-red">${seatButtonsHtml("red")}</div>
      <div class="team-col team-blue">${seatButtonsHtml("blue")}</div>`;
  }

  $all('[data-action="claim"]', seatArea).forEach((btn) => {
    btn.addEventListener("click", () => handleClaimSeat(btn.dataset.team, btn.dataset.role));
  });

  // Host remove-seat controls (× on player chips)
  $all("[data-remove]").forEach((btn) => {
    btn.addEventListener("click", () => handleClearSeat(btn.dataset.remove));
  });

  // Host controls. Co-op / vs-AI modes auto-start when a clue giver is claimed,
  // so there's no manual "Start game" step – hide the panel entirely.
  const hostPanel = $("#host-panel");
  const isHost = state.me && state.me.is_host;
  hostPanel.classList.toggle("hidden", !isHost || coop);
  if (isHost && !coop) {
    const redReady = state.players.some((p) => p.team === "red" && p.role === "spymaster");
    const blueReady = state.players.some((p) => p.team === "blue" && p.role === "spymaster");
    const ready = redReady && blueReady;
    const hint = ready
      ? "Both teams have a clue giver – ready to start."
      : "Each team needs a clue giver before you can start.";
    $("#start-game-btn").disabled = !ready;
    $("#start-game-hint").textContent = hint;
  }
}

async function handleClaimSeat(team, role) {
  try {
    const { error } = await sb.rpc("claim_seat", {
      p_room_id: state.roomId,
      p_team: team,
      p_role: role,
    });
    if (error) throw error;
    await resyncRoom();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't claim that seat.");
  }
}

async function handleClearSeat(targetPlayerId) {
  try {
    const { error } = await sb.rpc("clear_seat", {
      p_room_id: state.roomId,
      p_target_player_id: targetPlayerId,
    });
    if (error) throw error;
    await resyncRoom();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't clear that seat.");
  }
}

async function handleStartGame() {
  const btn = $("#start-game-btn");
  btn.disabled = true;
  try {
    const { error } = await sb.rpc("start_game", { p_room_id: state.roomId });
    if (error) throw error;
    await resyncRoom();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't start the game.");
    btn.disabled = false;
  }
}

// ============================================================================
// GAME SCREEN
// ============================================================================

function initGameScreen() {
  $("#clue-form").addEventListener("submit", handleSubmitClue);
  $("#clue-number").addEventListener("focus", function() { this.select(); });
  $("#end-turn-btn").addEventListener("click", handleEndTurn);
  $("#end-turn-btn-top").addEventListener("click", handleEndTurn);
  $("#leave-game-btn-top").addEventListener("click", () => { clearSession(); showScreen("landing"); });
  $("#share-clue-btn").addEventListener("click", () => handleShareClue());
  $("#share-board-btn").addEventListener("click", handleShareBoard);
  $("#leave-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
  $("#new-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
  $("#share-result-btn").addEventListener("click", handleShareResult);
  $("#see-board-btn").addEventListener("click", () => {
    dismissWin(state.roomId); // remember this choice so the overlay stays closed
    $("#win-overlay").classList.add("hidden");
  });
}

function isTwoPlayer(room) {
  return room?.mode === "two_player" || room?.mode === "turn_by_turn";
}

function isAsyncMode(room) {
  return room?.mode === "turn_by_turn";
}

function isVsAI(room) {
  return room?.mode === "two_player_ai";
}

// Any mode where two humans share the blue side and pick clue-giver / receiver
// (co-op two-player, turn-by-turn, or vs-AI).
function isBlueTeamMode(room) {
  return isTwoPlayer(room) || isVsAI(room);
}

function isObserver() {
  return !!(state.me && !state.me.team && !state.me.role && state.room?.status === "in_progress");
}

function canReveal() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || !room.current_clue) return false;
  if (room.mode === "in_person") return me.is_host || me.team === room.current_team;
  if (isVsAI(room)) return me.role === "operative" && room.current_team === "blue";
  if (isTwoPlayer(room)) return me.role === "operative";
  return me.team === room.current_team && me.role === "operative";
}

function canPass() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || !room.current_clue) return false;
  if (room.mode === "in_person") return me.is_host || me.team === room.current_team;
  if (isVsAI(room)) return me.role === "operative" && room.current_team === "blue";
  if (isTwoPlayer(room)) return me.role === "operative";
  return me.team === room.current_team && me.role === "operative";
}

function canGiveClue() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || room.current_clue) return false;
  if (isVsAI(room)) return me.role === "spymaster" && room.current_team === "blue";
  if (isTwoPlayer(room)) return me.role === "spymaster";
  return me.role === "spymaster" && me.team === room.current_team;
}

function renderGame(changedPosition) {
  const room = state.room;
  if (!room) return;
  const is2p = isTwoPlayer(room);
  const isAsync = isAsyncMode(room);
  const isAi = isVsAI(room);
  const coop = is2p || isAi; // two humans share the blue side
  // vs-AI: current_team === 'red' means the AI's turn is pending (waiting for the
  // client to trigger its reveal after a short "thinking" pause).
  const aiThinking = isAi && room.status === "in_progress" && room.current_team === "red";

  // --- Detect newly revealed tiles for animation + sound effects -----------
  const revealedNow = new Set(state.cards.filter((c) => c.revealed).map((c) => c.position));
  let newlyRevealed = [];
  if (state.revealedSnapshot === null) {
    state.revealedSnapshot = revealedNow; // first render for this room – seed, don't animate
  } else {
    newlyRevealed = [...revealedNow].filter((p) => !state.revealedSnapshot.has(p));
    // Put the tile the local player just clicked first so it animates before AI tiles.
    if (changedPosition != null && newlyRevealed.includes(changedPosition)) {
      newlyRevealed = [changedPosition, ...newlyRevealed.filter((p) => p !== changedPosition)];
    }
    state.revealedSnapshot = revealedNow;
  }

  // Sound: reveal outcomes
  if (newlyRevealed.length) {
    const byPos = Object.fromEntries(state.cards.map((c) => [c.position, c]));
    const cols = newlyRevealed.map((p) => byPos[p]?.revealed_colour);
    const myTeam = coop ? "blue" : (state.me?.team || room.current_team);
    if (cols.includes("assassin")) playSound("assassin");
    else if (isAi) {
      if (cols.includes("neutral")) playSound("wrong");
      else if (cols.includes("red")) playSound("ai");
      else if (cols.includes("blue")) playSound("correct");
    } else if (cols.some((c) => c && c !== myTeam)) playSound("wrong");
    else if (cols.some((c) => c === myTeam)) playSound("correct");
  }

  // Sound: a new clue was submitted
  const cc = room.clue_count ?? 0;
  if (state._prevClueCount != null && cc > state._prevClueCount) playSound("clue");
  state._prevClueCount = cc;

  // Sound: game just ended
  if (state._prevStatus && state._prevStatus !== "finished" && room.status === "finished") {
    if (room.winner === null) { /* assassin sound already played on the reveal */ }
    else if (isAi) playSound(room.winner === "blue" ? "win" : "lose");
    else playSound("win");
  }
  state._prevStatus = room.status;

  // Detect turn ending (clue cleared) to auto-share in async mode
  const prevClue = state._prevClue;
  state._prevClue = room.current_clue ?? null;
  if (prevClue && !room.current_clue && isAsync && state.me?.role === "operative" && room.status === "in_progress") {
    handleShareBoard();
  }

  // Turn banner
  const banner = $("#turn-banner");
  banner.classList.remove("team-red", "team-blue");
  if (room.status === "in_progress") {
    banner.classList.add(`team-${room.current_team}`);
    $("#turn-team-value").textContent = coop
      ? room.current_clue ? "GUESSING" : "CLUE GIVER'S TURN"
      : `${room.current_team.toUpperCase()} TEAM'S TURN`;
  } else {
    $("#turn-team-value").textContent = room.status === "finished" ? "Game over" : "–";
  }

  // vs-AI: show the AI's turn and, once, trigger its reveal after a short pause
  // so the AI feels deliberate. Only the clue receiver's client triggers it.
  if (aiThinking) {
    $("#turn-team-value").textContent = "🤖 AI'S TURN";
    if (state.me?.role === "operative" && !aiTurnTimer) {
      aiTurnTimer = setTimeout(async () => {
        aiTurnTimer = null;
        try {
          const { error } = await sb.rpc("ai_take_turn", { p_room_id: state.roomId });
          if (error) throw error;
          await resyncRoom();
        } catch (err) { console.error(err); }
      }, 2500);
    }
  } else if (aiTurnTimer) {
    clearTimeout(aiTurnTimer);
    aiTurnTimer = null;
  }

  // Timer
  renderTimer();

  // Clue readout (word + number)
  const clueReadout = $("#clue-readout");
  if (room.current_clue) {
    clueReadout.classList.remove("hidden");
    $("#clue-word-value").textContent = `${room.current_clue.word}, ${room.current_clue.number}`;
    const guessesLeft = room.guesses_remaining >= 99 ? "∞" : room.guesses_remaining;
    $("#clue-count-value").textContent = `${guessesLeft} guess${room.guesses_remaining === 1 ? "" : "es"} left`;
    // Snapshot which tiles are already revealed when this clue first appears,
    // so we can tell the operative what they guessed when they share the board.
    const clueId = `${room.current_clue.word}:${room.current_clue.number}:${room.clue_count}`;
    if (state.lastClueWord !== clueId) {
      state.lastClueWord = clueId;
      state.turnStartRevealed = new Set(state.cards.filter((c) => c.revealed).map((c) => c.position));
    }
  } else {
    clueReadout.classList.add("hidden");
  }

  // Observer / spy banners (mutually exclusive)
  const spyBanner = $("#spy-banner");
  const observerBanner = $("#observer-banner");
  const isGiver = state.me && state.me.role === "spymaster";
  const observer = isObserver();
  spyBanner.classList.add("hidden"); // removed – not useful to display
  observerBanner.classList.toggle("hidden", !observer);
  const legend = $("#board-legend");
  legend.classList.toggle("hidden", !isGiver);
  $("#legend-red").classList.toggle("hidden", is2p); // co-op two-player has no red team (vs-AI does)

  // Clue form
  $("#clue-form").classList.toggle("hidden", !canGiveClue());

  // Waiting-for-clue line
  const waiting = $("#waiting-for-clue");
  if (aiThinking) {
    waiting.classList.remove("hidden");
    waiting.textContent = "🤖 The AI is choosing its tiles…";
  } else if (room.status === "in_progress" && !room.current_clue && !canGiveClue()) {
    waiting.classList.remove("hidden");
    waiting.textContent = coop
      ? "Waiting for the clue giver's clue..."
      : `Waiting for the ${room.current_team} clue giver's clue...`;
  } else {
    waiting.classList.add("hidden");
  }

  // End turn buttons (top + bottom)
  $("#end-turn-btn").classList.toggle("hidden", !canPass());
  $("#end-turn-btn-top").classList.toggle("hidden", !canPass());

  // Share clue – only for the clue giver, and only while a clue is active
  const isSpymaster = state.me?.role === "spymaster";
  const hasClue = room.status === "in_progress" && !!room.current_clue;
  $("#share-clue-row").classList.toggle("hidden", !(isSpymaster && hasClue));

  // Share board – for operatives between turns; and for everyone once the game
  // is over (so the final board + summary can be shared).
  const isOperative = state.me?.role === "operative";
  const betweenTurns = room.status === "in_progress" && !room.current_clue;
  const finished = room.status === "finished";
  const shareBtn = $("#share-board-btn");
  if (shareBtn) shareBtn.textContent = finished ? "↗ Share result" : "↗ Share board";
  $("#share-board-row").classList.toggle("hidden", !((isOperative && betweenTurns) || finished));

  // Board
  renderBoardInto($("#board"), { interactive: true, animatePositions: newlyRevealed });

  // In-game team roster (always visible so players know who's who)
  renderGameTeams(room);

  // Clue log
  renderClueLog(room);

  // How-to-play banner
  renderModeExplainer(room);

  // Counts / rounds
  const redLeft = countRemaining(room, "red");
  const blueLeft = countRemaining(room, "blue");
  if (is2p) {
    $("#count-red-wrap").classList.add("hidden");
    $("#count-blue-wrap").classList.remove("hidden");
    $("#count-blue").textContent = blueLeft === null ? "–" : blueLeft;
    $("#round-wrap").classList.remove("hidden");
    $("#round-count").textContent = room.clue_count ?? 0;
  } else {
    $("#count-red-wrap").classList.remove("hidden");
    $("#count-blue-wrap").classList.remove("hidden");
    $("#round-wrap").classList.add("hidden");
    $("#count-red").textContent = redLeft === null ? "–" : redLeft;
    $("#count-blue").textContent = blueLeft === null ? "–" : blueLeft;
  }

  // Win / lose overlay – but respect a prior "See the board" dismissal so the
  // overlay doesn't pop back up when the player returns to the tab/app.
  const winOverlay = $("#win-overlay");
  if (room.status === "finished" && !isWinDismissed(state.roomId)) {
    winOverlay.classList.remove("hidden");
    const card = $("#win-card");
    card.classList.remove("win-red", "win-blue");
    if (isAi) {
      if (room.winner === "blue") {
        card.classList.add("win-blue");
        $("#win-title").textContent = `You beat the AI in ${room.clue_count} round${room.clue_count === 1 ? "" : "s"}!`;
        $("#win-subtitle").textContent = "Great teamwork – you cleared your Pokémon first.";
      } else if (room.winner === "red") {
        card.classList.add("win-red");
        $("#win-title").textContent = "The AI won!";
        $("#win-subtitle").textContent = "The AI cleared its tiles first – try an easier setting or a sharper clue.";
      } else {
        $("#win-title").textContent = "You hit the assassin!";
        $("#win-subtitle").textContent = "The assassin got you – better luck next time.";
      }
    } else if (is2p) {
      if (room.winner === "blue") {
        card.classList.add("win-blue");
        $("#win-title").textContent = `Cleared in ${room.clue_count} round${
          room.clue_count === 1 ? "" : "s"
        }!`;
        if (!statsRequested) {
          $("#win-subtitle").textContent = twoPlayerMessage(room.clue_count);
          fetchTwoPlayerStats(room.clue_count);
        }
      } else {
        $("#win-title").textContent = "You hit the assassin!";
        $("#win-subtitle").textContent = "The assassin got you – better luck next time.";
      }
    } else {
      card.classList.add(`win-${room.winner}`);
      $("#win-title").textContent = `${(room.winner || "").toUpperCase()} TEAM WINS`;
      $("#win-subtitle").textContent = "";
    }
  } else {
    winOverlay.classList.add("hidden");
  }
}

function countRemaining(room, team) {
  if (!room.starting_team) return null;
  const total = team === room.starting_team ? 9 : 8;
  const revealed = state.cards.filter((c) => c.revealed && c.revealed_colour === team).length;
  return total - revealed;
}

// ----------------------------------------------------------------------------
// Timer
// ----------------------------------------------------------------------------
function formatDuration(ms, long = false) {
  const s = Math.max(0, Math.floor(ms / 1000));
  if (!long) {
    const m = Math.floor(s / 60);
    return `${m}:${String(s % 60).padStart(2, "0")}`;
  }
  const d = Math.floor(s / 86400);
  const h = Math.floor((s % 86400) / 3600);
  const m = Math.floor((s % 3600) / 60);
  const ss = s % 60;
  const parts = [];
  if (d) parts.push(`${d}d`);
  if (h || d) parts.push(`${h}h`);
  if (m || h || d) parts.push(`${m}m`);
  parts.push(`${ss}s`);
  return parts.join(" ");
}

function renderTimer() {
  const el = $("#turn-timer");
  const room = state.room;
  if (!el || !room) return;

  const isAsync = isAsyncMode(room);
  const coop = isTwoPlayer(room) || isVsAI(room); // elapsed-time modes (timer starts on first clue)

  if (room.status === "in_progress") {
    if (coop) {
      // started_at is stamped on the first clue, so the timer only runs once
      // the game is actually underway.
      if (!room.started_at) { el.textContent = "Time elapsed: 0:00"; return; }
      const start = new Date(room.started_at).getTime();
      el.textContent = `Time elapsed: ${formatDuration(serverNow() - start, isAsync)}`;
    } else {
      const start = room.turn_started_at ? new Date(room.turn_started_at).getTime() : serverNow();
      el.textContent = `This turn: ${formatDuration(serverNow() - start)}`;
    }
  } else if (room.status === "finished" && coop) {
    const start = room.started_at ? new Date(room.started_at).getTime() : 0;
    const end = room.finished_at ? new Date(room.finished_at).getTime() : serverNow();
    el.textContent = start ? `Total time: ${formatDuration(end - start, isAsync)}` : "";
  } else {
    el.textContent = "";
  }
}

// ----------------------------------------------------------------------------
// In-game team roster
// ----------------------------------------------------------------------------
function renderGameTeams(room) {
  const el = $("#game-teams");
  const is2p = isTwoPlayer(room);
  const isAi = isVsAI(room);

  const playerRow = (p) => {
    const roleLabel = p.role === "spymaster" ? "clue giver" : p.role === "operative" ? "receiver" : "";
    const meTag = p.id === state.playerId ? " (you)" : "";
    return `<div class="gt-player"><span>${escapeHtml(p.nickname)}${escapeHtml(meTag)}</span>${
      roleLabel ? `<span class="gt-role">${roleLabel}</span>` : ""
    }</div>`;
  };

  const observers = state.players.filter((p) => !p.team && !p.role);
  const observersHtml = observers.length
    ? `<div class="gt-col gt-observers"><div class="gt-title">Observers</div>${observers.map(playerRow).join("")}</div>`
    : "";

  if (isAi) {
    // Humans are blue; the opponent is the AI (red).
    const blue = state.players.filter((p) => p.team === "blue");
    el.classList.remove("hidden");
    el.innerHTML = `
      <div class="gt-col gt-blue"><div class="gt-title">Your team</div>${blue.length ? blue.map(playerRow).join("") : '<div class="gt-player" style="color:var(--text-faint)">–</div>'}</div>
      <div class="gt-col gt-red"><div class="gt-title">AI opponent</div><div class="gt-player"><span>🤖 Computer</span><span class="gt-role">${escapeHtml(room.settings?.ai_difficulty || "easy")}</span></div></div>
      ${observersHtml}`;
  } else if (is2p) {
    const bluePlayers = state.players.filter((p) => p.team === "blue");
    if (bluePlayers.length === 0 && observers.length === 0) { el.classList.add("hidden"); return; }
    el.classList.remove("hidden");
    el.innerHTML = `<div class="gt-col gt-single"><div class="gt-title">Players</div>${bluePlayers.map(playerRow).join("")}</div>${observersHtml}`;
  } else {
    const red = state.players.filter((p) => p.team === "red");
    const blue = state.players.filter((p) => p.team === "blue");
    if (red.length === 0 && blue.length === 0 && observers.length === 0) { el.classList.add("hidden"); return; }
    el.classList.remove("hidden");
    el.innerHTML = `
      <div class="gt-col gt-red"><div class="gt-title">Red team</div>${red.length ? red.map(playerRow).join("") : '<div class="gt-player" style="color:var(--text-faint)">–</div>'}</div>
      <div class="gt-col gt-blue"><div class="gt-title">Blue team</div>${blue.length ? blue.map(playerRow).join("") : '<div class="gt-player" style="color:var(--text-faint)">–</div>'}</div>
      ${observersHtml}`;
  }
}

// ----------------------------------------------------------------------------
// How-to-play banner – a short reminder of the mode's dynamic, under the log
// ----------------------------------------------------------------------------
const MODE_EXPLAINERS = {
  online: "<strong>Classic online.</strong> Two teams race to find their own Pokémon. Each team's clue giver gives a one-word clue and a number; guessers tap tiles – find your team's, avoid the other team's, the neutrals, and never the assassin.",
  in_person: "<strong>In person.</strong> This screen shows the board for everyone. Each team's clue giver peeks at the key privately on their own phone and gives one-word clues; the group guesses on this shared screen.",
  two_player: "<strong>Two-player co-op.</strong> Work together to reveal all 9 of your blue Pokémon in as few rounds as possible. One gives clues, the other guesses. Hit the assassin and it's game over.",
  turn_by_turn: "<strong>Turn-by-turn co-op.</strong> Same as two-player, played at your own pace: the clue giver sends a clue, then shares the link so the guesser can take their turn whenever they like.",
  two_player_ai: "<strong>Two-player vs AI.</strong> You're the blue team – clear all 9 of your blue Pokémon before the AI reveals all 8 of its red ones. After each of your turns the AI flips over some red tiles. Avoid the assassin!",
};

function renderModeExplainer(room) {
  const el = $("#mode-explainer");
  if (!el) return;
  const text = MODE_EXPLAINERS[room.mode];
  if (!text) { el.classList.add("hidden"); return; }
  el.classList.remove("hidden");
  el.innerHTML = text;
}

// ----------------------------------------------------------------------------
// Clue log
// ----------------------------------------------------------------------------
function renderClueLog(room) {
  const panel = $("#clue-log");
  const list = $("#clue-log-list");
  const clueLog = Array.isArray(room.clue_log) ? room.clue_log : [];
  const guessLog = Array.isArray(room.guess_log) ? room.guess_log : [];
  if (clueLog.length === 0) {
    panel.classList.add("hidden");
    return;
  }
  panel.classList.remove("hidden");
  const is2p = isTwoPlayer(room);
  list.innerHTML = clueLog
    .map((c, i) => {
      let headerHtml;
      if (is2p) {
        headerHtml = `<div class="clue-log-row"><span class="cl-turn">Turn ${i + 1}</span><span class="cl-word">${escapeHtml(c.word)}</span><span class="cl-num">× ${c.number}</span></div>`;
      } else {
        const teamClass = c.team === "red" ? "cl-red" : "cl-blue";
        headerHtml = `<div class="clue-log-row"><span class="cl-dot ${teamClass}"></span><span class="cl-word">${escapeHtml(c.word)}</span><span class="cl-num">× ${c.number}</span></div>`;
      }
      const guesses = guessLog.filter((g) => g.clue_index === i);
      const guessesHtml = guesses
        .map((g) => {
          if (g.ai) {
            // The AI revealing one of its own red tiles on its turn.
            return `<div class="clue-log-row clue-guess"><span class="cl-ai">🤖</span><span class="cl-guess-name">${escapeHtml(g.name)}</span><span class="cl-colour-red">red</span></div>`;
          }
          const iconClass = g.correct ? "cl-correct" : "cl-wrong";
          const icon = g.correct ? "✓" : "✗";
          return `<div class="clue-log-row clue-guess"><span class="${iconClass}">${icon}</span><span class="cl-guess-name">${escapeHtml(g.name)}</span><span class="cl-colour-${g.colour}">${g.colour}</span></div>`;
        })
        .join("");
      return headerHtml + guessesHtml;
    })
    .join("");
}

// ----------------------------------------------------------------------------
// Two-player result messages + stats
// ----------------------------------------------------------------------------
function twoPlayerMessage(turns) {
  if (turns <= 1) return "*Pikachu surprised face*";
  if (turns === 2) return "Okay... that's ridiculous! You've played this game too much";
  if (turns === 3) return "Amazing! How did you manage that!?";
  if (turns === 4) return "Wow! Now that's some impressive team chemistry!";
  if (turns === 5) return "Nice play! That's a solid score";
  if (turns === 6) return "Okay, that's not too bad";
  return "You can do better than that.";
}

async function fetchTwoPlayerStats() {
  if (statsRequested) return;
  statsRequested = true;
  try {
    const { data, error } = await sb.rpc("record_two_player_result", { p_room_id: state.roomId });
    if (error) throw error;
    const row = data[0];
    const msg = twoPlayerMessage(row.your_turns);
    const statLine =
      row.total_games > 1
        ? `<br>You finished faster than ${row.faster_pct}% of players.`
        : `<br>You're the first to finish – a record to beat!`;
    $("#win-subtitle").innerHTML = `${escapeHtml(msg)}${statLine}`;
  } catch (err) {
    console.error(err);
  }
}

// ----------------------------------------------------------------------------
// Share helpers
// ----------------------------------------------------------------------------
function roomUrl() {
  const code = state.room?.code;
  if (!code) return window.location.href;
  const url = new URL(window.location.href);
  url.search = "";
  url.hash = "";
  url.searchParams.set("code", code);
  return url.toString();
}

async function nativeShare(payload) {
  if (navigator.share) {
    try { await navigator.share(payload); return; } catch (_) { /* user cancelled or not supported */ }
  }
  // Fallback: copy text to clipboard
  const text = [payload.title, payload.text, payload.url].filter(Boolean).join("\n");
  await navigator.clipboard.writeText(text);
  toast("Copied to clipboard!");
}

async function handleShareClue(word, number) {
  const clue = word != null ? { word, number } : state.room?.current_clue;
  if (!clue) return;
  const url = roomUrl();
  const text = `Clue: ${clue.word} × ${clue.number}\nIt's your turn to guess!`;
  await nativeShare({ title: "Pokémon Codenames", text, url });
}

function buildEmojiGrid() {
  const EMOJI = { red: "🟥", blue: "🟦", neutral: "🟨", assassin: "⬛", unrevealed: "⬜" };
  const sorted = [...state.cards].sort((a, b) => a.position - b.position);
  const rows = [];
  for (let r = 0; r < 5; r++) {
    rows.push(sorted.slice(r * 5, r * 5 + 5).map((c) => c.revealed ? (EMOJI[c.revealed_colour] ?? EMOJI.neutral) : EMOJI.unrevealed).join(""));
  }
  return rows.join("\n");
}

// Full end-of-game recap: final grid + every clue with its guesses (✅/❌),
// plus the outcome headline.
function buildResultShareText() {
  const room = state.room;
  const grid = buildEmojiGrid();
  const clueLog = Array.isArray(room.clue_log) ? room.clue_log : [];
  const guessLog = Array.isArray(room.guess_log) ? room.guess_log : [];

  let outcome;
  if (isVsAI(room)) {
    outcome = room.winner === "blue" ? `Beat the AI (${room.settings?.ai_difficulty || "easy"}) in ${room.clue_count} rounds!`
            : room.winner === "red" ? `Lost to the AI (${room.settings?.ai_difficulty || "easy"}).`
            : `Hit the assassin! 💀`;
  } else if (isTwoPlayer(room)) {
    outcome = room.winner === "blue" ? `Cleared the board in ${room.clue_count} rounds!` : `Hit the assassin! 💀`;
  } else {
    outcome = `${(room.winner || "").toUpperCase()} team wins!`;
  }

  const lines = [`Pokémon Codenames`, outcome, grid, ""];
  clueLog.forEach((c, i) => {
    lines.push(`${i + 1}. "${c.word}" ×${c.number}`);
    guessLog.filter((g) => g.clue_index === i).forEach((g) => {
      // AI guesses get the same robot marker used on the board / clue log.
      const who = g.ai ? "🤖 " : "";
      lines.push(`   ${g.correct ? "✅" : "❌"} ${who}${g.name}`);
    });
  });
  return lines.join("\n");
}

async function handleShareResult() {
  await nativeShare({
    title: "Pokémon Codenames – result",
    text: buildResultShareText(),
    url: roomUrl(),
  });
}

async function handleShareBoard() {
  // Once the game is finished, "Share board" becomes a full result recap.
  if (state.room?.status === "finished") return handleShareResult();

  const url = roomUrl();
  const room = state.room;
  const is2p = isTwoPlayer(room) || isVsAI(room);
  const myTeam = is2p ? "blue" : state.me?.team;

  // Work out what was guessed this turn using the snapshot taken when the clue arrived
  const thisRoundCards = state.cards.filter((c) => c.revealed && !state.turnStartRevealed.has(c.position));
  const correct = thisRoundCards.filter((c) => c.revealed_colour === myTeam).length;
  const wrong = thisRoundCards.filter((c) => c.revealed_colour !== myTeam).length;

  // Remaining team tiles – computed from the revealed cards so it's accurate.
  const remaining = countRemaining(room, is2p ? "blue" : myTeam);

  const grid = buildEmojiGrid();

  const turnSummary = [];
  if (correct > 0) turnSummary.push(`${correct} correct`);
  if (wrong > 0) turnSummary.push(`${wrong} wrong`);
  const turnLine = turnSummary.length ? `This turn: ${turnSummary.join(", ")}` : "";
  const teamColour = is2p ? "blue" : myTeam;
  const remainLine = remaining != null ? `${remaining} ${teamColour} tile${remaining === 1 ? "" : "s"} left to find` : "";

  const text = [
    `Pokémon Codenames`,
    grid,
    [turnLine, remainLine].filter(Boolean).join(" · "),
    `Your turn:`,
  ].filter(Boolean).join("\n");

  await nativeShare({ title: "Pokémon Codenames – board update", text, url });
}

// ----------------------------------------------------------------------------
// Game actions
// ----------------------------------------------------------------------------
function clueOverlapsPokemon(clue) {
  const norm = (s) => s.toLowerCase().replace(/[^a-z]/g, "");
  const clueNorm = norm(clue);
  if (!clueNorm) return null;
  for (const card of (state.cards || [])) {
    const name = norm(card.name);
    if (!name) continue;
    if ((name.includes(clueNorm) && clueNorm.length > 3) || (clueNorm.includes(name) && name.length > 3)) return card.name;
  }
  return null;
}

async function handleSubmitClue(e) {
  e.preventDefault();
  const word = $("#clue-word").value.trim();
  const number = Number($("#clue-number").value);
  if (!word) return;
  const overlap = clueOverlapsPokemon(word);
  if (overlap) {
    toast(`"${word}" overlaps with "${overlap}" on the board. Pick a different clue.`);
    return;
  }
  const btn = $("#submit-clue-btn");
  btn.disabled = true;
  try {
    const { error } = await sb.rpc("submit_clue", {
      p_room_id: state.roomId,
      p_word: word,
      p_number: number,
    });
    if (error) throw error;
    await resyncRoom();
    if (isAsyncMode(state.room) || isVsAI(state.room)) await handleShareClue(word, number);
    $("#clue-word").value = "";
    $("#clue-number").value = "1";
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't submit that clue.");
  } finally {
    btn.disabled = false;
  }
}

let _revealInProgress = false;
async function handleRevealCard(position) {
  if (_revealInProgress) return;
  _revealInProgress = true;
  const hadClue = !!state.room?.current_clue;
  try {
    const { error } = await sb.rpc("reveal_card", { p_room_id: state.roomId, p_position: position });
    if (error) throw error;
    await resyncRoom(position);
    // vs-AI: if that guess ended the turn, auto-open the board share for the
    // clue receiver (matches the pass-to-share behaviour of turn-by-turn).
    if (isVsAI(state.room) && state.me?.role === "operative" && hadClue && !state.room?.current_clue) {
      await handleShareBoard();
    }
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't reveal that tile.");
  } finally {
    _revealInProgress = false;
  }
}

async function handleEndTurn() {
  try {
    const { error } = await sb.rpc("end_turn", { p_room_id: state.roomId });
    if (error) throw error;
    await resyncRoom();
    if (isAsyncMode(state.room) || isVsAI(state.room)) await handleShareBoard();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't pass the turn.");
  }
}

// ----------------------------------------------------------------------------
// Utilities
// ----------------------------------------------------------------------------
function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str ?? "";
  return div.innerHTML;
}

// ============================================================================
// DAILY PUZZLE (1 player)
// ============================================================================
const daily = {
  pool: null, date: null, tiles: [], clues: [], revealedHints: [],
  revealed: {}, // position -> colour
  bluesFound: 0, bluesTotal: 9, mistakes: 0, maxMistakes: 5, hintsUsed: 0,
  shownHintIdx: [], noMoreHints: false,
  startedAt: null, finished: false, outcome: null, solution: null, solutionClues: null,
  taps: [], attemptId: null, rating: null,
};

// Difficulty label derived from the puzzle's clue-category spread (change #2).
// More Category-1 (easy type/colour) clues => easier; more Category-4/5
// (lore/stat/anti) clues => harder.
function dailyDifficulty(clues) {
  const cats = (clues || []).map((c) => c.cat || 1);
  const ones = cats.filter((c) => c === 1).length;
  const highs = cats.filter((c) => c >= 4).length;
  if (highs >= 4) return { label: "Evil", cls: "evil" };
  if (highs >= 3) return { label: "Brutal", cls: "brutal" };
  if (ones === 0) return { label: "Hard", cls: "hard" };
  if (ones === 1) return { label: "Challenging", cls: "challenging" };
  if (ones === 2) return { label: "Medium", cls: "medium" };
  return { label: "Easy", cls: "easy" };
}

function initDaily() {
  $("#daily-gen1-btn").addEventListener("click", () => startDaily("gen1"));
  $("#daily-mixed-btn").addEventListener("click", () => startDaily("mixed"));
  $("#daily-exit-btn").addEventListener("click", () => { showScreen("landing"); });
  $("#daily-hint-btn").addEventListener("click", dailyRequestHint);
}

function _dailyReset() {
  daily.tiles = []; daily.clues = []; daily.revealedHints = [];
  daily.revealed = {}; daily.bluesFound = 0; daily.mistakes = 0; daily.hintsUsed = 0;
  daily.shownHintIdx = []; daily.noMoreHints = false;
  daily.startedAt = null; daily.finished = false; daily.outcome = null;
  daily.solution = null; daily.solutionClues = null;
  daily.taps = []; daily.attemptId = null; daily.rating = null;
}

async function startDaily(pool) {
  try {
    await ensureAuth();
    const { data, error } = await sb.rpc("get_daily_puzzle", { p_pool: pool });
    if (error) throw error;
    const row = data && data[0];
    if (!row) { toast("No daily puzzle available yet – check back soon."); return; }
    _dailyReset();
    daily.pool = pool;
    daily.date = row.puzzle_date;
    daily.clues = row.clues || [];
    daily.tiles = (row.tiles || []).slice().sort((a, b) => a.position - b.position);
    daily.bluesTotal = 9;
    daily.startedAt = Date.now(); // timer starts as soon as the puzzle loads
    setRoomPill(null);
    showScreen("daily");
    renderDaily();
    // Log the start of this attempt (best-effort).
    try {
      const { data: aid } = await sb.rpc("daily_start_attempt", { p_date: daily.date, p_pool: pool });
      daily.attemptId = aid || null;
    } catch (err) { console.error(err); }
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't load the daily puzzle.");
  }
}

function _clueChip(c) {
  // Note: c.cat (difficulty 1-5) is a back-end categorisation only – not shown.
  if (c.anti) {
    return `<div class="daily-clue daily-anti"><span class="dc-word">${escapeHtml(c.word)}</span><span class="dc-num">× 0</span></div>`;
  }
  return `<div class="daily-clue"><span class="dc-word">${escapeHtml(c.word)}</span><span class="dc-num">× ${c.number}</span></div>`;
}

function renderDaily() {
  const poolLabel = daily.pool === "gen1" ? "Gen I" : "All generations";
  const diff = dailyDifficulty(daily.clues);
  $("#daily-play-title").innerHTML =
    `Daily puzzle – ${poolLabel} <span class="daily-diff diff-${diff.cls}">${diff.label}</span>`;
  $("#daily-play-sub").textContent = daily.date
    ? `Find all 9 blue Pokémon. 5 strikes and you're out.` : "";

  // Stat bar
  const secs = daily.startedAt ? Math.floor((Date.now() - daily.startedAt) / 1000) : 0;
  const time = `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`;
  $("#daily-statbar").innerHTML =
    `<span>🔵 <strong>${daily.bluesFound}</strong>/9 found</span>` +
    `<span>✗ <strong>${daily.mistakes}</strong>/${daily.maxMistakes} strikes</span>` +
    `<span>💡 <strong>${daily.hintsUsed}</strong> hints</span>` +
    `<span>⏱ <strong id="daily-timer">${time}</strong></span>`;

  // Clues (base + revealed hints)
  const cluesHtml = daily.clues.map(_clueChip).join("");
  const hintsHtml = daily.revealedHints.length
    ? `<div class="daily-hints-label">Extra clues</div>` + daily.revealedHints.map(_clueChip).join("")
    : "";
  $("#daily-clues").innerHTML = cluesHtml + hintsHtml;

  // Hint button – extra clues are now unlimited and chosen to match the tiles
  // you still have left, so it stays available until no helpful clue remains.
  const hintBtn = $("#daily-hint-btn");
  hintBtn.textContent = daily.hintsUsed
    ? `💡 Reveal another clue (${daily.hintsUsed} shown)`
    : `💡 Reveal an extra clue`;
  hintBtn.disabled = daily.finished || daily.noMoreHints;
  hintBtn.classList.toggle("hidden", daily.finished);

  // Board
  renderDailyBoard();

  // Result
  const result = $("#daily-result");
  if (daily.finished) { result.classList.remove("hidden"); renderDailyResult(); }
  else result.classList.add("hidden");
}

function dailyMakeTile(tile) {
  const el = document.createElement("div");
  el.className = "tile";
  const colour = daily.revealed[tile.position] || (daily.finished && daily.solution
    ? (daily.solution.find((s) => s.position === tile.position) || {}).colour : null);
  const revealedByPlayer = !!daily.revealed[tile.position];
  if (colour) { el.classList.add("revealed"); el.dataset.colour = colour; }
  if (daily.finished && colour && !revealedByPlayer) el.classList.add("daily-unpicked");

  const clickable = !daily.finished && !daily.revealed[tile.position];
  if (!clickable && !colour) el.classList.add("locked");

  const art = tile.sprite_url || (tile.pokemon_id ? `${ART_BASE}/${tile.pokemon_id}.png` : "");
  const fallback = tile.pokemon_id ? `${SPRITE_BASE}/${tile.pokemon_id}.png` : "";
  el.innerHTML = `
    <div class="tile-img-wrap"><img src="${art}" alt="${escapeHtml(tile.name)}" decoding="async" ${fallback ? `onerror="this.onerror=null;this.src='${fallback}'"` : ""} /></div>
    <div class="tile-name">${escapeHtml(tile.name)}</div>`;
  if (clickable) el.addEventListener("click", () => dailyRevealTile(tile.position));
  return el;
}

function renderDailyBoard() {
  const board = $("#daily-board");
  board.innerHTML = "";
  daily.tiles.forEach((t) => board.appendChild(dailyMakeTile(t)));
}

let _dailyRevealBusy = false;
async function dailyRevealTile(position) {
  if (daily.finished || daily.revealed[position] || _dailyRevealBusy) return;
  _dailyRevealBusy = true;
  try {
    const { data, error } = await sb.rpc("daily_reveal", {
      p_date: daily.date, p_pool: daily.pool, p_position: position,
    });
    if (error) throw error;
    const colour = data;
    daily.revealed[position] = colour;
    const tile = daily.tiles.find((t) => t.position === position);
    daily.taps.push({ position, name: tile ? tile.name : null, colour });

    if (colour === "assassin") {
      playSound("assassin");
      renderDaily();
      dailyFinish("assassin");
    } else if (colour === "blue") {
      daily.bluesFound += 1;
      playSound("correct");
      if (daily.bluesFound >= daily.bluesTotal) { renderDaily(); dailyFinish("win"); }
      else renderDaily();
    } else {
      daily.mistakes += 1;
      playSound("wrong");
      if (daily.mistakes >= daily.maxMistakes) { renderDaily(); dailyFinish("lose"); }
      else renderDaily();
    }
  } catch (err) {
    console.error(err);
    toast("Couldn't reveal that tile.");
  } finally {
    _dailyRevealBusy = false;
  }
}

async function dailyRequestHint() {
  if (daily.finished || daily.noMoreHints) return;
  // Ask the server for the next clue that helps with a tile we HAVEN'T revealed
  // yet (change #4). It picks from clues covering the most still-missing blues,
  // so late-game hints naturally narrow to the specific tiles left.
  const revealed = Object.keys(daily.revealed).map(Number);
  try {
    const { data, error } = await sb.rpc("daily_hint_next", {
      p_date: daily.date, p_pool: daily.pool,
      p_revealed: revealed, p_shown: daily.shownHintIdx,
    });
    if (error) throw error;
    if (!data) { daily.noMoreHints = true; toast("No more helpful clues right now."); renderDaily(); return; }
    daily.revealedHints.push(data);
    if (typeof data.idx === "number") daily.shownHintIdx.push(data.idx);
    daily.hintsUsed += 1;
    renderDaily();
  } catch (err) {
    // Fallback for older puzzles/DBs without the conditional-hint RPC: serve
    // the flat hint list by index (old behaviour, capped at 3).
    console.error(err);
    try {
      if (daily.hintsUsed >= 3) { daily.noMoreHints = true; renderDaily(); return; }
      const { data, error } = await sb.rpc("daily_hint", {
        p_date: daily.date, p_pool: daily.pool, p_index: daily.hintsUsed,
      });
      if (error) throw error;
      if (!data) { daily.noMoreHints = true; toast("No more extra clues for this puzzle."); renderDaily(); return; }
      daily.revealedHints.push(data);
      daily.hintsUsed += 1;
      renderDaily();
    } catch (err2) {
      console.error(err2);
      toast("Couldn't get an extra clue.");
    }
  }
}

async function dailyFinish(outcome) {
  daily.finished = true;
  daily.outcome = outcome;
  if (outcome === "win") playSound("win");
  else if (outcome === "lose") playSound("lose");
  const duration = daily.startedAt ? Date.now() - daily.startedAt : 0;
  try {
    const { data, error } = await sb.rpc("daily_solution", { p_date: daily.date, p_pool: daily.pool });
    if (!error && data) {
      // New shape: { tiles, clues (with targets) }. Old shape: a bare tiles array.
      if (Array.isArray(data)) { daily.solution = data; daily.solutionClues = null; }
      else { daily.solution = data.tiles || []; daily.solutionClues = data.clues || null; }
    }
  } catch (err) { console.error(err); }
  // Log the finished attempt (best-effort).
  if (daily.attemptId) {
    try {
      await sb.rpc("daily_finish_attempt", {
        p_id: daily.attemptId, p_outcome: outcome, p_blues: daily.bluesFound,
        p_mistakes: daily.mistakes, p_hints: daily.hintsUsed, p_duration: duration,
        p_taps: daily.taps,
      });
    } catch (err) { console.error(err); }
  }
  renderDaily();
}

function renderDailyResult() {
  const el = $("#daily-result");
  const secs = daily.startedAt ? Math.floor((Date.now() - daily.startedAt) / 1000) : 0;
  const time = `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`;
  let title;
  if (daily.outcome === "win") title = `Solved it! 9/9 🎉`;
  else if (daily.outcome === "assassin") title = `💀 You hit the assassin!`;
  else title = `Out of guesses – ${daily.bluesFound}/9 found`;

  // Show what each clue was pointing to (change #5), now the board's revealed.
  let answersHtml = "";
  if (daily.solutionClues && daily.solution) {
    const nameAt = {};
    daily.solution.forEach((t) => (nameAt[t.position] = t.name));
    const rows = daily.solutionClues.map((c) => {
      const num = c.anti ? "× 0" : `× ${c.number}`;
      const names = c.anti
        ? "anti-clue – none of your Pokémon"
        : (c.t || []).map((p) => escapeHtml(nameAt[p] || "?")).join(", ");
      return `<div class="daily-answer-row"><span class="da-clue">${escapeHtml(c.word)} <span class="da-num">${num}</span></span><span class="da-names">${names}</span></div>`;
    }).join("");
    answersHtml = `<div class="daily-answers"><div class="daily-answers-label">What each clue meant</div>${rows}</div>`;
  }

  const ratings = [
    ["way_too_easy", "Way too easy"],
    ["slightly_easy", "Slightly easy"],
    ["just_right", "Just right"],
    ["slightly_hard", "Slightly hard"],
    ["way_too_hard", "Way too hard"],
  ];
  const rateBtns = ratings
    .map(([v, label]) => `<button class="btn btn-ghost btn-mini daily-rate ${daily.rating === v ? "chosen" : ""}" data-rate="${v}">${label}</button>`)
    .join("");
  el.innerHTML = `
    <div class="daily-result-title">${title}</div>
    <div class="daily-result-line">🔵 ${daily.bluesFound}/9 · ✗ ${daily.mistakes} strikes · 💡 ${daily.hintsUsed} hints · ⏱ ${time}</div>
    ${answersHtml}
    <div class="daily-rate-label">${daily.rating ? "Thanks for the feedback!" : "How was the difficulty?"}</div>
    <div class="daily-rate-row">${rateBtns}</div>
    <div class="daily-result-btns">
      <button class="btn btn-share" id="daily-share-btn">↗ Share result</button>
      <button class="btn btn-ghost" id="daily-other-btn">Play the ${daily.pool === "gen1" ? "All-gens" : "Gen I"} puzzle</button>
      <button class="btn btn-ghost" id="daily-home-btn">Home</button>
    </div>`;
  $("#daily-share-btn").addEventListener("click", dailyShare);
  $("#daily-other-btn").addEventListener("click", () => startDaily(daily.pool === "gen1" ? "mixed" : "gen1"));
  $("#daily-home-btn").addEventListener("click", () => showScreen("landing"));
  $all(".daily-rate", el).forEach((b) => b.addEventListener("click", () => dailyRate(b.dataset.rate)));
}

async function dailyRate(rating) {
  daily.rating = rating;
  renderDailyResult();
  if (daily.attemptId) {
    try { await sb.rpc("daily_rate_attempt", { p_id: daily.attemptId, p_rating: rating }); }
    catch (err) { console.error(err); }
  }
}

function dailyShare() {
  // No board grid – that would reveal the answers to whoever you share with
  // (change #3). Share only the outcome, mistakes, guesses and time.
  const secs = daily.startedAt ? Math.floor((Date.now() - daily.startedAt) / 1000) : 0;
  const time = `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`;
  const poolLabel = daily.pool === "gen1" ? "Gen I" : "All gens";
  const diff = dailyDifficulty(daily.clues);
  const outcome = daily.outcome === "win"
    ? `✅ Solved it – all 9 found!`
    : `❌ ${daily.bluesFound}/9 found`;
  const text = [
    `Pokémon Codenames – Daily (${poolLabel} · ${diff.label})`,
    outcome,
    `✗ ${daily.mistakes} mistakes · ⏱ ${time}`,
    `Can you beat it?`,
  ].join("\n");
  const url = `${window.location.origin}${window.location.pathname}`;
  nativeShare({ title: "Pokémon Codenames – Daily", text, url });
}

// ============================================================================
// Boot
// ============================================================================
async function boot() {
  initLandingScreen();
  initLobbyScreen();
  initGameScreen();
  initSoundToggle();
  initDaily();

  $("#refresh-btn").addEventListener("click", async () => {
    await resyncRoom();
    toast("Refreshed.");
  });

  await ensureAuth();
  await syncRealtimeAuth();
  await syncServerClock();
  sb.auth.onAuthStateChange(() => syncRealtimeAuth());

  // Self-healing: on focus/visibility, on a steady background interval, and a
  // once-a-second tick just to keep the timer display moving.
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") resyncRoom();
  });
  window.addEventListener("focus", () => resyncRoom());
  setInterval(pollTick, POLL_MS);
  setInterval(() => {
    if (state.room && $("#screen-game").classList.contains("active")) renderTimer();
    if ($("#screen-daily").classList.contains("active") && daily.startedAt && !daily.finished) {
      const el = $("#daily-timer");
      if (el) {
        const secs = Math.floor((Date.now() - daily.startedAt) / 1000);
        el.textContent = `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`;
      }
    }
  }, 1000);

  _migrateOldSession(); // one-time migration from old single-session key

  const inviteCode = new URLSearchParams(window.location.search).get("code");
  if (inviteCode) {
    // If we already have a session for this room code, jump straight in
    const saved = _findSessionForCode(inviteCode);
    if (saved) {
      state.roomId = saved.roomId;
      state.playerId = saved.playerId;
      state.nickname = saved.nickname || "";
      try {
        await enterRoom();
        return;
      } catch (err) {
        console.error(err);
        _removeSession(saved.roomId);
        // fall through to quick-join overlay
      }
    }
    // No saved session for this code – show quick-join overlay
    const el = $("#quick-join-code");
    el.textContent = inviteCode.toUpperCase();
    el.dataset.code = inviteCode.toUpperCase();
    $("#quick-join-overlay").classList.remove("hidden");
    return;
  }

  // No invite code – restore the most recently visited game ONLY if it's still
  // in progress. Landing on the bare site URL should open the homepage, not
  // reopen the end-of-game banner of a game that's already finished. We peek at
  // the room status first so a finished game never even flashes on screen.
  const last = _findLastSession();
  if (last) {
    state.roomId = last.roomId;
    state.playerId = last.playerId;
    state.nickname = last.nickname || "";
    try {
      await fetchRoom();
      if (state.room && state.room.status !== "finished") {
        await enterRoom();
        return;
      }
      // Finished (or unreadable): fall through to the homepage. Keep the stored
      // session so a ?code deep-link can still reopen it later.
      state.room = null;
      state.roomId = null;
      state.playerId = null;
    } catch (err) {
      console.error(err);
      _removeSession(last.roomId);
    }
  }

  showScreen("landing");
}

boot();
