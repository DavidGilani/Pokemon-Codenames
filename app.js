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
  _cluePhase: null, // classic mode: {key, at} anchor for the clue-giving timer
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
  state._cluePhase = null;
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
      // Classic per-turn timer. turn_started_at is stamped when the clue is
      // submitted, so during the clue giver's thinking phase it's null – anchor
      // to when we first saw this clue-giving turn so the timer keeps running
      // instead of sitting at 0:00.
      let start;
      if (room.turn_started_at) {
        start = new Date(room.turn_started_at).getTime();
      } else {
        const key = `${room.current_team}:${room.clue_count || 0}`;
        if (!state._cluePhase || state._cluePhase.key !== key) {
          state._cluePhase = { key, at: serverNow() };
        }
        start = state._cluePhase.at;
      }
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
  // Timer as an accumulator of ACTIVE time so it can pause when the player
  // leaves the tab/app: elapsedMs = banked active time; runningSince = when the
  // current active stretch began (null while paused/finished); timerOn = started.
  elapsedMs: 0, runningSince: null, timerOn: false,
  // Offline play: `sealed` is the obfuscated blob from the server; `key` is the
  // unsealed { c: {pos->colour}, h: hints[], k: clues[] }. When `key` is set,
  // every reveal / hint / finish is resolved locally with no further network,
  // so a dropped connection after load doesn't stop the puzzle.
  sealed: null, key: null,
  // Player's own scratch notes (per device, never sent anywhere): `clueDone`
  // is a set of clue ids the player greyed out; `clueLeft` maps a clue id to how
  // many of its tiles the player thinks are still to find (0..number); `notes`
  // maps a tile position to an array of clue indices (colours) pencilled on it.
  clueDone: {}, clueLeft: {}, notes: {},
  // Tutorial "test game": a self-contained example board played fully offline.
  // Nothing is saved, logged or shareable; finishing offers today's real puzzles.
  practice: false,
  // QA / playtest mode (URL-gated ?qa=1): play upcoming boards back-to-back and
  // save a rating + note per board to the daily_feedback table. Like practice,
  // nothing is cached to localStorage and no player attempt is logged. `qaQueue`
  // and `qaIndex` persist across boards (not cleared by _dailyReset).
  qa: false, qaQueue: [], qaIndex: 0,
};

// One vivid colour per base clue, by display order. Used both to tint the clue
// chips and as the pencil-marking palette on tiles (Clues-by-Sam style).
const DAILY_CLUE_COLORS = ["#e5484d", "#f5a524", "#46c26a", "#3fb6e0", "#c150c8"];

// Un-seal the offline puzzle blob (mirror of _daily_seal in SQL): base64-decode,
// XOR with the shared key, then parse. Kept deliberately lightweight — this is
// obfuscation so the answers aren't readable at a glance, not real encryption.
const DAILY_SEAL_KEY = [142, 55, 91, 44, 116, 17, 163];
function _dailyUnseal(b64) {
  const bin = atob(String(b64).replace(/\s+/g, "")); // Postgres base64 wraps at 76 cols

  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i) ^ DAILY_SEAL_KEY[i % 7];
  return JSON.parse(new TextDecoder().decode(out));
}
// A stable signature of a board (tile names + clue words). If the puzzle for a
// date/pool is re-authored (e.g. a mid-day difficulty change), the signature
// changes, so a cached "completed"/in-progress record for the OLD board is
// ignored and the player can attempt the new one.
function _dailySig(tiles, clues) {
  const t = (tiles || []).map((x) => x.name).sort().join("|");
  const c = (clues || []).map((x) => x.word).sort().join("|");
  const s = t + "#" + c;
  let h = 5381;
  for (let i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) >>> 0;
  return h.toString(36);
}
// Base clues for mid-game display, with the answer-bearing fields removed.
function _dailyStripClues(clues) {
  return (clues || []).map((c) => {
    const o = { word: c.word, number: c.number, cat: c.cat };
    if (c.anti) o.anti = true;
    return o;
  });
}
// The next most-helpful unshown hint, computed locally (mirror of
// daily_hint_next): prefer the hint covering the most STILL-unrevealed blues,
// tie-break easier category first, then order.
function _dailyNextHintLocal() {
  const revealed = Object.keys(daily.revealed).map(Number);
  const hints = (daily.key && daily.key.h) || [];
  let best = null;
  hints.forEach((hint, idx) => {
    if (daily.shownHintIdx.includes(idx)) return;
    const t = hint.t || [];
    const unrev = t.filter((p) => !revealed.includes(p)).length;
    if (unrev <= 0) return;
    const cat = hint.cat || 1;
    if (!best || unrev > best.unrev || (unrev === best.unrev && cat < best.cat)) {
      best = { idx, unrev, cat, hint };
    }
  });
  if (!best) return null;
  return { word: best.hint.word, number: best.hint.number, cat: best.hint.cat || 1, idx: best.idx };
}
// Find a saved-but-still-current daily for this pool (used to resume offline if
// the initial fetch fails). Returns the parsed record, or null.
function _latestSavedForPool(pool) {
  try {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && k.startsWith(DAILY_KEY_PREFIX) && k.endsWith(":" + pool)) {
        const s = JSON.parse(localStorage.getItem(k));
        if (s && s.pool === pool && s.sealed) return s;
      }
    }
  } catch {}
  return null;
}

// Active elapsed time (ms/secs), counting only while the timer is running.
function dailyElapsedMs() {
  return daily.elapsedMs + (daily.runningSince && !daily.finished ? Date.now() - daily.runningSince : 0);
}
function dailyElapsedSecs() { return Math.floor(dailyElapsedMs() / 1000); }
function fmtClock(secs) { return `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`; }
// Local YYYY-MM-DD, optionally offset by N days (used to build the QA date window).
function _todayStr(offsetDays) {
  const d = new Date();
  if (offsetDays) d.setDate(d.getDate() + offsetDays);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

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

// Deep-link suffix for each daily pool, so a finished puzzle can be shared:
// ?daily=1 (Gen I) and ?daily=all (mixed / all generations).
function dailyParam(pool) { return pool === "gen1" ? "1" : "all"; }
function poolFromParam(v) { return v === "1" ? "gen1" : v === "all" ? "mixed" : null; }
function dailyUrl(pool) {
  return `${window.location.origin}${window.location.pathname}?daily=${dailyParam(pool)}`;
}
function setDailyUrl(pool) {
  try { history.replaceState(null, "", `${window.location.pathname}?daily=${dailyParam(pool)}`); } catch {}
}
function clearDailyUrl() {
  try { history.replaceState(null, "", window.location.pathname); } catch {}
}

// --- Per-device daily progress (no login): remember how far a player got in
// each day's puzzle, keyed by puzzle date + pool, in localStorage. Restoring a
// finished puzzle re-shows the stats box; restoring an in-progress one puts the
// board, strikes, hints and timer back where they were.
const DAILY_KEY_PREFIX = "pc_daily:";
function _dailyKey(date, pool) { return `${DAILY_KEY_PREFIX}${date}:${pool}`; }
function _saveDailyProgress() {
  if (daily.practice || daily.qa) return; // the tutorial and QA games are never cached
  if (!daily.date || !daily.pool) return;
  try {
    localStorage.setItem(_dailyKey(daily.date, daily.pool), JSON.stringify({
      v: 1, date: daily.date, pool: daily.pool,
      revealed: daily.revealed, bluesFound: daily.bluesFound, mistakes: daily.mistakes,
      hintsUsed: daily.hintsUsed, revealedHints: daily.revealedHints, shownHintIdx: daily.shownHintIdx,
      noMoreHints: daily.noMoreHints, taps: daily.taps, elapsedMs: dailyElapsedMs(),
      finished: daily.finished, outcome: daily.outcome, solution: daily.solution,
      solutionClues: daily.solutionClues, attemptId: daily.attemptId, rating: daily.rating,
      sealed: daily.sealed, sig: daily.sig,
      clueDone: daily.clueDone, clueLeft: daily.clueLeft, notes: daily.notes,
    }));
  } catch {}
  _pruneDailyProgress();
}
function _loadDailyProgress(date, pool) {
  try {
    const raw = localStorage.getItem(_dailyKey(date, pool));
    if (!raw) return null;
    const s = JSON.parse(raw);
    return (s && s.date === date && s.pool === pool) ? s : null;
  } catch { return null; }
}
function _pruneDailyProgress() {
  // Drop saved dailies from earlier days (date is YYYY-MM-DD, so string compare
  // is chronological). Keeps localStorage tidy — only the current date survives.
  try {
    for (let i = localStorage.length - 1; i >= 0; i--) {
      const k = localStorage.key(i);
      if (k && k.startsWith(DAILY_KEY_PREFIX)) {
        const d = k.slice(DAILY_KEY_PREFIX.length).split(":")[0];
        if (d && daily.date && d < daily.date) localStorage.removeItem(k);
      }
    }
  } catch {}
}

// Pause/resume the daily timer (banks active time on pause; only resumes while
// the daily screen is actually showing). Idempotent, so repeated events are safe.
function dailyPauseTimer() {
  if (daily.timerOn && daily.runningSince != null && !daily.finished) {
    daily.elapsedMs += Date.now() - daily.runningSince;
    daily.runningSince = null;
    _saveDailyProgress();
  }
}
function dailyResumeTimer() {
  if (daily.timerOn && daily.runningSince == null && !daily.finished
      && $("#screen-daily").classList.contains("active")) {
    daily.runningSince = Date.now();
  }
}

function initDaily() {
  $("#daily-gen1-btn").addEventListener("click", () => startDaily("gen1"));
  $("#daily-mixed-btn").addEventListener("click", () => startDaily("mixed"));
  $("#daily-exit-btn").addEventListener("click", () => { _closeNotePalette(); dailyPauseTimer(); daily.qa = false; daily.qaQueue = []; daily.qaIndex = 0; clearDailyUrl(); showScreen("landing"); });
  $("#daily-hint-btn").addEventListener("click", dailyRequestHint);
  $("#daily-tutorial-btn").addEventListener("click", startPractice);
}

function _dailyReset() {
  daily.tiles = []; daily.clues = []; daily.revealedHints = [];
  daily.revealed = {}; daily.bluesFound = 0; daily.mistakes = 0; daily.hintsUsed = 0;
  daily.shownHintIdx = []; daily.noMoreHints = false;
  daily.startedAt = null; daily.finished = false; daily.outcome = null;
  daily.solution = null; daily.solutionClues = null;
  daily.taps = []; daily.attemptId = null; daily.rating = null;
  daily.elapsedMs = 0; daily.runningSince = null; daily.timerOn = false;
  daily.sealed = null; daily.key = null; daily.sig = null;
  daily.clueDone = {}; daily.clueLeft = {}; daily.notes = {}; _closeNotePalette();
  daily.practice = false;
  daily.qa = false; // qaQueue/qaIndex intentionally left alone (span multiple boards)
}

// A fixed, self-contained example board used by the "Play a test game" tutorial
// — the real Wed 19 Aug Gen I daily (fossils, shells, horns, Cubone the orphan,
// Machamp's arms), chosen to show off non-type clues. Colours/clues/hints live
// entirely client-side (like an unsealed daily) so it plays with zero network
// and is never cached.
const PRACTICE_BLUES = [
  [2, "Nidoking", 34], [3, "Cubone", 104], [4, "Kabutops", 141], [5, "Machamp", 68],
  [9, "Rhydon", 112], [13, "Psyduck", 54], [16, "Aerodactyl", 142], [18, "Omastar", 139],
  [20, "Starmie", 121],
];
const PRACTICE_NEUTRALS = [
  [0, "Pikachu", 25], [1, "Gengar", 94], [6, "Weezing", 110], [7, "Ninetales", 38],
  [8, "Haunter", 93], [10, "Snorlax", 143], [11, "Koffing", 109], [12, "Jolteon", 135],
  [14, "Meowth", 52], [15, "Arcanine", 59], [17, "Electabuzz", 125], [19, "Vulpix", 37],
  [21, "Vaporeon", 134], [22, "Growlithe", 58], [23, "Persian", 53], [24, "Raichu", 26],
];
const PRACTICE_CLUES = [
  { word: "FOSSIL", number: 3, cat: 4, t: [4, 16, 18], explain: "They were all revived from prehistoric fossils." },
  { word: "MISTY", number: 2, cat: 3, t: [13, 20], explain: "Both are on the team of Water-type gym leader Misty." },
  { word: "HORN", number: 2, cat: 2, t: [2, 9], explain: "Each has a prominent horn." },
  { word: "ORPHAN", number: 1, cat: 4, t: [3], explain: "Cubone wears the skull of its lost mother — the 'Lonely' Pokémon." },
  { word: "ARMS", number: 1, cat: 2, t: [5], explain: "Machamp and its four muscular arms." },
];
const PRACTICE_HINTS = [
  { word: "SICKLE", number: 1, cat: 2, t: [4], explain: "Kabutops slashes with its scythe-like blades." },
  { word: "SPIRAL", number: 1, cat: 2, t: [18], explain: "Omastar's coiled, spiral ammonite shell." },
  { word: "FANGS", number: 1, cat: 2, t: [16], explain: "The sharp fangs lining Aerodactyl's jaws." },
  { word: "HEADACHE", number: 1, cat: 4, t: [13], explain: "Psyduck's endless psychic headache." },
  { word: "GEM", number: 1, cat: 2, t: [20], explain: "The jewelled core at the centre of Starmie." },
  { word: "DRILL", number: 1, cat: 2, t: [9], explain: "The drill-like horn on Rhydon's snout." },
  { word: "ROYALTY", number: 1, cat: 4, t: [2], explain: "‘King’ is right there in Nidoking's name." },
  { word: "SKULL", number: 1, cat: 2, t: [3], explain: "The skull helmet Cubone wears." },
  { word: "MUSCLE", number: 1, cat: 3, t: [5], explain: "Machamp's four bulging arms." },
];

function startPractice() {
  _closeNotePalette();
  dailyPauseTimer();
  _dailyReset();
  daily.practice = true;
  daily.pool = "gen1"; // keeps internal helpers happy; the UI shows "Test game"
  daily.date = "practice";
  daily.bluesTotal = 9;
  const tiles = [];
  const c = {};
  PRACTICE_BLUES.forEach(([pos, name, id]) => { tiles.push({ name, pokemon_id: id, position: pos }); c[String(pos)] = "blue"; });
  PRACTICE_NEUTRALS.forEach(([pos, name, id]) => { tiles.push({ name, pokemon_id: id, position: pos }); c[String(pos)] = "neutral"; });
  tiles.sort((a, b) => a.position - b.position);
  daily.tiles = tiles;
  daily.key = { c, h: PRACTICE_HINTS, k: PRACTICE_CLUES };
  daily.clues = _dailyStripClues(PRACTICE_CLUES);
  daily.sig = _dailySig(daily.tiles, daily.clues);
  daily.startedAt = Date.now();
  daily.elapsedMs = 0; daily.runningSince = Date.now(); daily.timerOn = true;
  clearDailyUrl();
  showScreen("daily");
  renderDaily();
}

async function startDaily(pool) {
  try {
    try { await ensureAuth(); } catch (e) { console.error(e); } // may fail offline; carry on
    let date = null, tiles = null, sealed = null, cluesOnline = null;
    // Preferred path: get the whole puzzle "sealed" so it can be played offline.
    try {
      const { data, error } = await sb.rpc("get_daily_full", { p_pool: pool });
      if (error) throw error;
      const row = data && data[0];
      if (row) {
        date = row.puzzle_date;
        tiles = (row.tiles || []).slice().sort((a, b) => a.position - b.position);
        sealed = row.sealed || null;
      }
    } catch (e) { console.error(e); }
    // Fallback: older DB without get_daily_full → colour-hidden online mode.
    if (!date) {
      try {
        const { data, error } = await sb.rpc("get_daily_puzzle", { p_pool: pool });
        if (error) throw error;
        const row = data && data[0];
        if (row) {
          date = row.puzzle_date;
          tiles = (row.tiles || []).slice().sort((a, b) => a.position - b.position);
          cluesOnline = row.clues || [];
        }
      } catch (e) { console.error(e); }
    }
    // Last resort: fully offline at load — resume the most recent saved puzzle
    // for this pool if we cached its sealed blob earlier.
    if (!date) {
      const s = _latestSavedForPool(pool);
      if (s) { date = s.date; sealed = s.sealed; }
    }
    if (!date) { toast("No daily puzzle available yet – check back soon."); return; }

    _dailyReset();
    daily.pool = pool;
    daily.date = date;
    daily.bluesTotal = 9;
    if (sealed) {
      daily.sealed = sealed;
      try { daily.key = _dailyUnseal(sealed); } catch (e) { console.error(e); daily.key = null; }
    }
    daily.clues = daily.key ? _dailyStripClues(daily.key.k) : (cluesOnline || []);
    if (tiles) daily.tiles = tiles;
    daily.sig = _dailySig(daily.tiles, daily.clues);
    setRoomPill(null);
    setDailyUrl(pool); // reflect which daily this is in the URL (shareable)

    // Already played (or partway through) on this device today? Restore it and
    // DON'T start a new attempt or reset the timer. A finished puzzle re-opens
    // straight to the stats box; an in-progress one resumes where it left off.
    // BUT if the board was re-authored since (signature changed — e.g. a mid-day
    // difficulty swap), ignore the stale record and start the new puzzle fresh.
    const saved = _loadDailyProgress(daily.date, pool);
    if (saved && saved.sig && daily.sig && saved.sig !== daily.sig) {
      try { localStorage.removeItem(_dailyKey(daily.date, pool)); } catch {}
    } else if (saved) {
      daily.revealed = saved.revealed || {};
      daily.bluesFound = saved.bluesFound || 0;
      daily.mistakes = saved.mistakes || 0;
      daily.hintsUsed = saved.hintsUsed || 0;
      daily.revealedHints = saved.revealedHints || [];
      daily.shownHintIdx = saved.shownHintIdx || [];
      daily.noMoreHints = !!saved.noMoreHints;
      daily.taps = saved.taps || [];
      daily.elapsedMs = saved.elapsedMs || 0;
      daily.finished = !!saved.finished;
      daily.outcome = saved.outcome || null;
      daily.solution = saved.solution || null;
      daily.solutionClues = saved.solutionClues || null;
      daily.attemptId = saved.attemptId || null;
      daily.rating = saved.rating || null;
      daily.clueDone = saved.clueDone || {};
      daily.clueLeft = saved.clueLeft || {};
      daily.notes = saved.notes || {};
      daily.timerOn = !daily.finished;
      daily.runningSince = daily.finished ? null : Date.now();
      showScreen("daily");
      renderDaily();
      return;
    }

    // Fresh start: timer begins now (as active time), then render + log.
    daily.startedAt = Date.now();
    daily.elapsedMs = 0; daily.runningSince = Date.now(); daily.timerOn = true;
    showScreen("daily");
    renderDaily();
    // Log the start of this attempt (best-effort).
    try {
      const { data: aid } = await sb.rpc("daily_start_attempt", { p_date: daily.date, p_pool: pool });
      daily.attemptId = aid || null;
    } catch (err) { console.error(err); }
    _saveDailyProgress();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't load the daily puzzle.");
  }
}

// ============================================================================
// QA / playtest mode (change #5) — URL-gated with ?qa=1. Loads every board in a
// date window and plays them back-to-back with the normal daily engine; after
// each board the tester leaves a rating + note, saved to the daily_feedback
// table (read back here via Supabase to fix boards). Nothing is cached locally
// and no player attempt is logged.
// ============================================================================
const QA_WINDOW_DAYS = 30; // how far ahead to pull upcoming boards for QA

async function startQaBatch() {
  try {
    try { await ensureAuth(); } catch (e) { console.error(e); }
    const from = _todayStr();
    const to = _todayStr(QA_WINDOW_DAYS);
    const { data, error } = await sb.rpc("list_daily_qa", { p_from: from, p_to: to });
    if (error) throw error;
    const all = (data || []).map((r) => ({
      date: r.puzzle_date, pool: r.pool, n_clues: r.n_clues, difficulty: r.difficulty,
      reviewed: r.reviewed || 0,
    }));
    // Only queue boards that haven't been QA'd yet (no feedback saved for them).
    const queue = all.filter((b) => !b.reviewed);
    const skipped = all.length - queue.length;
    if (!queue.length) {
      toast(all.length
        ? `All ${all.length} upcoming boards have already been QA'd. 🎉`
        : "No upcoming boards to QA in the next 30 days.");
      showScreen("landing");
      return;
    }
    if (skipped) toast(`Skipping ${skipped} already-QA'd board${skipped === 1 ? "" : "s"}.`);
    daily.qaQueue = queue;
    daily.qaIndex = 0;
    await qaLoadCurrent();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't load the QA batch.");
    showScreen("landing");
  }
}

async function qaLoadCurrent() {
  if (daily.qaIndex >= daily.qaQueue.length) { renderQaDone(); return; }
  const item = daily.qaQueue[daily.qaIndex];
  await startQaBoard(item.date, item.pool);
}

async function startQaBoard(date, pool) {
  try {
    let tiles = null, sealed = null;
    const { data, error } = await sb.rpc("get_daily_qa", { p_date: date, p_pool: pool });
    if (error) throw error;
    const row = data && data[0];
    if (!row) { toast(`No board found for ${date} (${pool}).`); daily.qaIndex++; return qaLoadCurrent(); }
    tiles = (row.tiles || []).slice().sort((a, b) => a.position - b.position);
    sealed = row.sealed || null;

    _dailyReset();
    daily.qa = true;
    daily.pool = pool;
    daily.date = date;
    daily.bluesTotal = 9;
    if (sealed) {
      daily.sealed = sealed;
      try { daily.key = _dailyUnseal(sealed); } catch (e) { console.error(e); daily.key = null; }
    }
    daily.clues = daily.key ? _dailyStripClues(daily.key.k) : [];
    daily.tiles = tiles;
    daily.sig = _dailySig(daily.tiles, daily.clues);
    setRoomPill(null);
    clearDailyUrl();
    daily.startedAt = Date.now();
    daily.elapsedMs = 0; daily.runningSince = Date.now(); daily.timerOn = true;
    showScreen("daily");
    renderDaily();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't load the QA board.");
  }
}

async function qaSaveAndAdvance(outcome) {
  const item = daily.qaQueue[daily.qaIndex] || {};
  const note = ($("#qa-note") ? $("#qa-note").value : "").trim();
  const rating = daily.rating || null;
  try {
    await sb.rpc("submit_daily_feedback", {
      p_date: daily.date, p_pool: daily.pool,
      p_rating: rating, p_note: note,
      p_outcome: outcome || daily.outcome || null,
      p_mistakes: daily.mistakes, p_hints: daily.hintsUsed,
      p_duration: dailyElapsedSecs(),
    });
    toast("Feedback saved.");
  } catch (err) {
    console.error(err);
    toast("Couldn't save feedback (see console) — moving on.");
  }
  daily.qaIndex++;
  await qaLoadCurrent();
}

// Save the current board's feedback (best-effort) and leave QA mode for home.
async function qaSaveAndAdvanceThenExit() {
  const note = ($("#qa-note") ? $("#qa-note").value : "").trim();
  try {
    await sb.rpc("submit_daily_feedback", {
      p_date: daily.date, p_pool: daily.pool,
      p_rating: daily.rating || null, p_note: note,
      p_outcome: daily.outcome || null, p_mistakes: daily.mistakes,
      p_hints: daily.hintsUsed, p_duration: dailyElapsedSecs(),
    });
    toast("Feedback saved.");
  } catch (err) { console.error(err); }
  daily.qa = false; daily.qaQueue = []; daily.qaIndex = 0;
  clearDailyUrl();
  showScreen("landing");
}

function renderQaDone() {
  daily.qa = false; // batch over — leave QA mode
  const el = $("#daily-result");
  const n = daily.qaQueue.length;
  el.innerHTML = `
    <div class="daily-result-title">QA batch complete 🎉</div>
    <div class="daily-result-line">You reviewed ${n} board${n === 1 ? "" : "s"}. Feedback is saved.</div>
    <div class="daily-result-btns">
      <button class="btn btn-primary" id="qa-restart-btn">Run the batch again</button>
      <button class="btn btn-ghost" id="daily-home-btn">Home</button>
    </div>`;
  // Hide the mid-game play elements and show just the result panel.
  ["#daily-statbar", "#daily-clues", "#daily-board", "#daily-tutorial-row"].forEach((sel) => {
    const n = $(sel); if (n) n.classList.add("hidden");
  });
  const hintRow = document.querySelector(".daily-hint-row"); if (hintRow) hintRow.classList.add("hidden");
  el.classList.remove("hidden");
  $("#qa-restart-btn").addEventListener("click", startQaBatch);
  $("#daily-home-btn").addEventListener("click", () => { clearDailyUrl(); showScreen("landing"); });
}

function _clueChip(c, idx, kind) {
  // Note: c.cat (difficulty 1-5) is a back-end categorisation only – not shown.
  // `kind` is "b" (base clue) or "h" (revealed hint); base clues carry a colour
  // dot matching the tile-marking palette. Tapping a chip greys it out (a
  // personal "I've got this one" toggle) — see the delegated handler below.
  const id = `${kind}${idx}`;
  const done = daily.clueDone[id] ? " is-done" : "";
  const colour = kind === "b" ? DAILY_CLUE_COLORS[idx % DAILY_CLUE_COLORS.length] : null;
  const dot = colour ? `<span class="dc-dot" style="background:${colour}"></span>` : "";
  const anti = c.anti ? " daily-anti" : "";
  // The × number, optionally overridden by the player's own "still to find" count
  // (set by holding the chip). When reduced, the original is struck through.
  const left = daily.clueLeft[id];
  let num;
  if (c.anti) num = "× 0";
  else if (kind === "b" && typeof left === "number" && left !== c.number)
    num = `<s>× ${c.number}</s> <span class="dc-left">${left} left</span>`;
  else num = `× ${c.number}`;
  return `<div class="daily-clue${anti}${done}" data-clue-id="${id}" data-clue-num="${c.number}" data-clue-kind="${kind}" role="button" tabindex="0">`
    + `${dot}<span class="dc-word">${escapeHtml(c.word)}</span><span class="dc-num">${num}</span></div>`;
}

function renderDaily() {
  const poolLabel = daily.pool === "gen1" ? "Gen I" : "All generations";
  const diff = dailyDifficulty(daily.clues);
  // Un-hide the play elements (renderQaDone hides them at the end of a QA batch).
  ["#daily-statbar", "#daily-clues", "#daily-board"].forEach((sel) => {
    const n = $(sel); if (n) n.classList.remove("hidden");
  });
  const hRow = document.querySelector(".daily-hint-row"); if (hRow) hRow.classList.remove("hidden");
  if (daily.qa) {
    $("#daily-play-title").innerHTML =
      `QA ${daily.qaIndex + 1}/${daily.qaQueue.length} · ${poolLabel} `
      + `<span class="daily-diff diff-${diff.cls}">${diff.label}</span>`;
    $("#daily-play-sub").textContent = `${daily.date} — play it, then rate it.`;
  } else {
    $("#daily-play-title").innerHTML = daily.practice
      ? `Test game <span class="daily-diff diff-example">Example</span>`
      : `Daily puzzle – ${poolLabel} <span class="daily-diff diff-${diff.cls}">${diff.label}</span>`;
    $("#daily-play-sub").textContent = daily.practice
      ? `A quick example to learn the ropes — nothing here is saved or shared.`
      : (daily.date ? `Find all 9 blue Pokémon. 5 strikes and you're out.` : "");
  }
  // Tutorial affordances: the "test game" button shows on the real puzzle only;
  // the how-to-play panel shows only while playing the test game. QA hides both.
  const tutRow = $("#daily-tutorial-row");
  if (tutRow) tutRow.classList.toggle("hidden", daily.practice || daily.qa || daily.finished);
  const tutPanel = $("#daily-tutorial-panel");
  if (tutPanel) tutPanel.classList.toggle("hidden", !daily.practice || daily.finished);

  // Stat bar
  const time = fmtClock(dailyElapsedSecs());
  $("#daily-statbar").innerHTML =
    `<span>🔵 <strong>${daily.bluesFound}</strong>/9 found</span>` +
    `<span>✗ <strong>${daily.mistakes}</strong>/${daily.maxMistakes} strikes</span>` +
    `<span>💡 <strong>${daily.hintsUsed}</strong> hints</span>` +
    `<span>⏱ <strong id="daily-timer">${time}</strong></span>`;

  // Clues (base + revealed hints)
  const cluesHtml = daily.clues.map((c, i) => _clueChip(c, i, "b")).join("");
  const hintsHtml = daily.revealedHints.length
    ? `<div class="daily-hints-label">Extra clues</div>`
      + daily.revealedHints.map((c, j) => _clueChip(c, j, "h")).join("")
    : "";
  const cluesEl = $("#daily-clues");
  cluesEl.innerHTML = cluesHtml + hintsHtml;
  if (!cluesEl._noteWired) {
    cluesEl._noteWired = true;
    // Tap a clue to grey it out ("got this one"); press & hold a BASE clue to
    // set how many of its tiles you still have to find (0..number).
    const toggleDone = (chip) => {
      if (!chip || daily.finished) return;
      const id = chip.dataset.clueId;
      if (daily.clueDone[id]) delete daily.clueDone[id]; else daily.clueDone[id] = true;
      chip.classList.toggle("is-done");
      _saveDailyProgress();
    };
    let lpTimer = null, longFired = false, sx = 0, sy = 0;
    const cancelLP = () => { if (lpTimer) { clearTimeout(lpTimer); lpTimer = null; } };
    cluesEl.addEventListener("pointerdown", (e) => {
      const chip = e.target.closest(".daily-clue");
      if (!chip || daily.finished) return;
      if (e.pointerType === "mouse" && e.button !== 0) return;
      longFired = false; sx = e.clientX; sy = e.clientY;
      const num = Number(chip.dataset.clueNum);
      if (chip.dataset.clueKind === "b" && num > 0) {
        lpTimer = setTimeout(() => { longFired = true; openClueCountPalette(chip); }, 420);
      }
    });
    cluesEl.addEventListener("pointermove", (e) => {
      if (lpTimer && (Math.abs(e.clientX - sx) > 12 || Math.abs(e.clientY - sy) > 12)) cancelLP();
    });
    cluesEl.addEventListener("pointerup", cancelLP);
    cluesEl.addEventListener("pointercancel", cancelLP);
    cluesEl.addEventListener("pointerleave", cancelLP);
    cluesEl.addEventListener("contextmenu", (e) => {
      const chip = e.target.closest(".daily-clue");
      if (chip && chip.dataset.clueKind === "b" && !daily.finished) { e.preventDefault(); openClueCountPalette(chip); }
    });
    cluesEl.addEventListener("click", (e) => {
      if (longFired) { longFired = false; return; } // long-press already handled
      toggleDone(e.target.closest(".daily-clue"));
    });
    cluesEl.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggleDone(e.target.closest(".daily-clue")); }
    });
  }

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

  // Colour pencil-marks (the player's own scratch notes) — only while the tile
  // is still in play; once revealed/finished the real colour takes over.
  if (clickable) _renderTileNotes(el, tile.position);

  if (clickable) {
    // Short tap reveals; long-press (or right-click) opens the colour palette.
    // A long-press must NOT also reveal, so we swallow the trailing click.
    let lpTimer = null, longFired = false, sx = 0, sy = 0;
    const cancelLP = () => { if (lpTimer) { clearTimeout(lpTimer); lpTimer = null; } };
    el.addEventListener("pointerdown", (e) => {
      if (e.pointerType === "mouse" && e.button !== 0) return;
      longFired = false; sx = e.clientX; sy = e.clientY;
      lpTimer = setTimeout(() => { longFired = true; openNotePalette(tile.position, el); }, 420);
    });
    el.addEventListener("pointermove", (e) => {
      if (lpTimer && (Math.abs(e.clientX - sx) > 12 || Math.abs(e.clientY - sy) > 12)) cancelLP();
    });
    el.addEventListener("pointerup", cancelLP);
    el.addEventListener("pointercancel", cancelLP);
    el.addEventListener("pointerleave", cancelLP);
    el.addEventListener("contextmenu", (e) => { e.preventDefault(); openNotePalette(tile.position, el); });
    el.addEventListener("click", () => {
      if (longFired) { longFired = false; return; } // long-press already handled
      dailyRevealTile(tile.position);
    });
  }
  return el;
}

// Draw the little coloured corner triangles for whichever clues the player has
// pencilled onto this tile. Each clue colour has a fixed corner so a given
// colour always sits in the same spot across the board.
function _renderTileNotes(el, position) {
  const existing = el.querySelector(".tile-notes");
  if (existing) existing.remove();
  const marks = daily.notes[position] || [];
  if (!marks.length) return;
  const wrap = document.createElement("div");
  wrap.className = "tile-notes";
  marks.slice().sort((a, b) => a - b).forEach((ci) => {
    const m = document.createElement("span");
    m.className = `note-mark note-slot-${ci % 5}`;
    m.style.setProperty("--nc", DAILY_CLUE_COLORS[ci % DAILY_CLUE_COLORS.length]);
    wrap.appendChild(m);
  });
  el.appendChild(wrap);
}

// The floating colour-palette popover (one shared element). Long-pressing a tile
// opens it beside that tile; tapping a swatch toggles that clue-colour note.
let _notePaletteEl = null, _notePalettePos = null;
function _closeNotePalette() {
  if (_notePaletteEl) { _notePaletteEl.remove(); _notePaletteEl = null; }
  _notePalettePos = null;
  document.removeEventListener("pointerdown", _notePaletteOutside, true);
}
function _notePaletteOutside(e) {
  if (_notePaletteEl && !_notePaletteEl.contains(e.target)) _closeNotePalette();
}
function openNotePalette(position, tileEl) {
  if (daily.finished || daily.revealed[position]) return;
  _closeNotePalette();
  _notePalettePos = position;
  const pal = document.createElement("div");
  pal.className = "note-palette";
  const marks = daily.notes[position] || [];
  // A "clear" swatch, then one swatch per base clue colour.
  const clear = document.createElement("button");
  clear.className = "note-swatch note-clear"; clear.type = "button";
  clear.setAttribute("aria-label", "Clear marks");
  clear.addEventListener("click", () => {
    delete daily.notes[position];
    _renderTileNotes(tileEl, position); _saveDailyProgress(); _closeNotePalette();
  });
  pal.appendChild(clear);
  for (let i = 0; i < daily.clues.length; i++) {
    const sw = document.createElement("button");
    sw.type = "button"; sw.className = "note-swatch";
    sw.style.background = DAILY_CLUE_COLORS[i % DAILY_CLUE_COLORS.length];
    if (marks.includes(i)) sw.classList.add("is-on");
    sw.setAttribute("aria-label", `Clue ${i + 1}`);
    sw.addEventListener("click", () => {
      const cur = daily.notes[position] || [];
      const at = cur.indexOf(i);
      if (at >= 0) cur.splice(at, 1); else cur.push(i);
      if (cur.length) daily.notes[position] = cur; else delete daily.notes[position];
      sw.classList.toggle("is-on");
      _renderTileNotes(tileEl, position); _saveDailyProgress();
    });
    pal.appendChild(sw);
  }
  document.body.appendChild(pal);
  _notePaletteEl = pal;
  // Position beside the tile (to the right if it fits, else the left).
  const r = tileEl.getBoundingClientRect();
  const pr = pal.getBoundingClientRect();
  const sxo = window.scrollX, syo = window.scrollY;
  let left = r.right + sxo + 8;
  if (r.right + pr.width + 8 > window.innerWidth) left = r.left + sxo - pr.width - 8;
  let top = r.top + syo + (r.height - pr.height) / 2;
  top = Math.max(syo + 8, Math.min(top, syo + window.innerHeight - pr.height - 8));
  pal.style.left = `${Math.max(sxo + 4, left)}px`;
  pal.style.top = `${top}px`;
  setTimeout(() => document.addEventListener("pointerdown", _notePaletteOutside, true), 0);
}

// Press & hold a base clue to set how many of its tiles are still to find.
function openClueCountPalette(chip) {
  if (daily.finished) return;
  _closeNotePalette();
  const id = chip.dataset.clueId;
  const number = Number(chip.dataset.clueNum);
  const cur = (typeof daily.clueLeft[id] === "number") ? daily.clueLeft[id] : number;
  const pal = document.createElement("div");
  pal.className = "note-palette clue-count-palette";
  pal.innerHTML = `<div class="ccp-label">Still to find</div>`;
  const rowEl = document.createElement("div"); rowEl.className = "ccp-row";
  for (let k = 0; k <= number; k++) {
    const btn = document.createElement("button");
    btn.type = "button"; btn.className = "ccp-btn" + (k === cur ? " is-on" : "");
    btn.textContent = String(k);
    btn.addEventListener("click", () => {
      if (k === number) delete daily.clueLeft[id]; else daily.clueLeft[id] = k;
      renderDaily();           // re-render chips with the new count (also closes this)
      _saveDailyProgress();
    });
    rowEl.appendChild(btn);
  }
  pal.appendChild(rowEl);
  document.body.appendChild(pal);
  _notePaletteEl = pal;
  const r = chip.getBoundingClientRect();
  const pr = pal.getBoundingClientRect();
  const sxo = window.scrollX, syo = window.scrollY;
  let top = r.bottom + syo + 6;
  if (r.bottom + pr.height + 6 > window.innerHeight) top = r.top + syo - pr.height - 6;
  let leftpx = Math.max(sxo + 4, Math.min(r.left + sxo, sxo + window.innerWidth - pr.width - 4));
  pal.style.left = `${leftpx}px`; pal.style.top = `${Math.max(syo + 4, top)}px`;
  setTimeout(() => document.addEventListener("pointerdown", _notePaletteOutside, true), 0);
}

function renderDailyBoard() {
  _closeNotePalette();
  const board = $("#daily-board");
  board.innerHTML = "";
  daily.tiles.forEach((t) => board.appendChild(dailyMakeTile(t)));
}

let _dailyRevealBusy = false;
async function dailyRevealTile(position) {
  if (daily.finished || daily.revealed[position] || _dailyRevealBusy) return;
  _dailyRevealBusy = true;
  try {
    let colour;
    if (daily.key) {
      // Offline: colour comes from the unsealed key — no network.
      colour = (daily.key.c && daily.key.c[String(position)]) || "neutral";
    } else {
      const { data, error } = await sb.rpc("daily_reveal", {
        p_date: daily.date, p_pool: daily.pool, p_position: position,
      });
      if (error) throw error;
      colour = data;
    }
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
    _saveDailyProgress();
  } catch (err) {
    console.error(err);
    toast("Couldn't reveal that tile.");
  } finally {
    _dailyRevealBusy = false;
  }
}

async function dailyRequestHint() {
  if (daily.finished || daily.noMoreHints) return;
  // Offline: pick the next helpful hint locally from the unsealed key.
  if (daily.key) {
    const h = _dailyNextHintLocal();
    if (!h) { daily.noMoreHints = true; toast("No more helpful clues right now."); renderDaily(); _saveDailyProgress(); return; }
    daily.revealedHints.push(h);
    daily.shownHintIdx.push(h.idx);
    daily.hintsUsed += 1;
    renderDaily();
    _saveDailyProgress();
    return;
  }
  // Online: ask the server for the next clue that helps with a tile we HAVEN'T
  // revealed yet. It picks from clues covering the most still-missing blues, so
  // late-game hints naturally narrow to the specific tiles left.
  const revealed = Object.keys(daily.revealed).map(Number);
  try {
    const { data, error } = await sb.rpc("daily_hint_next", {
      p_date: daily.date, p_pool: daily.pool,
      p_revealed: revealed, p_shown: daily.shownHintIdx,
    });
    if (error) throw error;
    if (!data) { daily.noMoreHints = true; toast("No more helpful clues right now."); renderDaily(); _saveDailyProgress(); return; }
    daily.revealedHints.push(data);
    if (typeof data.idx === "number") daily.shownHintIdx.push(data.idx);
    daily.hintsUsed += 1;
    renderDaily();
    _saveDailyProgress();
  } catch (err) {
    // Fallback for older puzzles/DBs without the conditional-hint RPC: serve
    // the flat hint list by index (old behaviour, capped at 3).
    console.error(err);
    try {
      if (daily.hintsUsed >= 3) { daily.noMoreHints = true; renderDaily(); _saveDailyProgress(); return; }
      const { data, error } = await sb.rpc("daily_hint", {
        p_date: daily.date, p_pool: daily.pool, p_index: daily.hintsUsed,
      });
      if (error) throw error;
      if (!data) { daily.noMoreHints = true; toast("No more extra clues for this puzzle."); renderDaily(); _saveDailyProgress(); return; }
      daily.revealedHints.push(data);
      daily.hintsUsed += 1;
      renderDaily();
      _saveDailyProgress();
    } catch (err2) {
      console.error(err2);
      toast("Couldn't get an extra clue.");
    }
  }
}

async function dailyFinish(outcome) {
  // Freeze the timer at the current active time before anything else reads it.
  const duration = dailyElapsedMs();
  daily.elapsedMs = duration; daily.runningSince = null; daily.timerOn = false;
  daily.finished = true;
  daily.outcome = outcome;
  if (outcome === "win") playSound("win");
  else if (outcome === "lose") playSound("lose");
  if (daily.key) {
    // Offline: build the full reveal from the unsealed key — no network.
    daily.solution = daily.tiles.map((t) => ({
      ...t, colour: (daily.key.c && daily.key.c[String(t.position)]) || "neutral",
    }));
    daily.solutionClues = daily.key.k || null;
  } else {
    try {
      const { data, error } = await sb.rpc("daily_solution", { p_date: daily.date, p_pool: daily.pool });
      if (!error && data) {
        // New shape: { tiles, clues (with targets) }. Old shape: a bare tiles array.
        if (Array.isArray(data)) { daily.solution = data; daily.solutionClues = null; }
        else { daily.solution = data.tiles || []; daily.solutionClues = data.clues || null; }
      }
    } catch (err) { console.error(err); }
  }
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
  _saveDailyProgress(); // remember completion on this device
  renderDaily();
}

// The "What each clue meant" box: a row per base clue, then a row for each
// EXTRA CLUE the player revealed (with the tile it pointed to, and a why-line
// where the data carries one). Shared by the normal and tutorial finish screens.
function _dailyAnswersBox() {
  if (!daily.solutionClues || !daily.solution) return "";
  const nameAt = {};
  daily.solution.forEach((t) => (nameAt[t.position] = t.name));
  const row = (word, numTxt, names, explain, extraClass) =>
    `<div class="daily-answer-row${extraClass || ""}"><div class="da-line">`
    + `<span class="da-clue">${escapeHtml(word)}${numTxt ? ` <span class="da-num">${numTxt}</span>` : ""}</span>`
    + `<span class="da-names">${names}</span></div>`
    + (explain ? `<div class="da-why">${escapeHtml(explain)}</div>` : "") + `</div>`;

  const clueRows = daily.solutionClues.map((c) => {
    const num = c.anti ? "× 0" : `× ${c.number}`;
    const names = c.anti ? "anti-clue – none of your Pokémon"
      : (c.t || []).map((p) => escapeHtml(nameAt[p] || "?")).join(", ");
    return row(c.word, num, names, c.explain, "");
  }).join("");

  // Extra clues the player actually revealed. Prefer the full hint objects from
  // the unsealed key (they carry the target tile + any why-line); fall back to
  // whatever was shown mid-game.
  const keyHints = (daily.key && daily.key.h) || [];
  const revealed = (daily.shownHintIdx && daily.shownHintIdx.length)
    ? daily.shownHintIdx.map((i) => keyHints[i]).filter(Boolean)
    : (daily.revealedHints || []);
  let hintRows = "";
  if (revealed.length) {
    const rows = revealed.map((h) => {
      const names = (h.t || []).map((p) => escapeHtml(nameAt[p] || "?")).join(", ");
      return row(`💡 ${h.word}`, "", names, h.explain, " da-hint-row");
    }).join("");
    hintRows = `<div class="daily-answers-sublabel">Extra clues you revealed</div>${rows}`;
  }
  return `<div class="daily-answers"><div class="daily-answers-label">What each clue meant</div>${clueRows}${hintRows}</div>`;
}

function renderDailyResult() {
  const el = $("#daily-result");
  const time = fmtClock(dailyElapsedSecs());
  let title;
  if (daily.outcome === "win") title = `Solved it! 9/9 🎉`;
  else if (daily.outcome === "assassin") title = `💀 You hit the assassin!`;
  else title = `Out of guesses – ${daily.bluesFound}/9 found`;

  const answersHtml = _dailyAnswersBox();

  // QA finish: show the outcome + answers, then a rating + note form. Saving
  // writes to daily_feedback and advances to the next board in the batch.
  if (daily.qa) {
    const ratings = [
      ["way_too_easy", "Way too easy"], ["slightly_easy", "Slightly easy"],
      ["just_right", "Just right"], ["slightly_hard", "Slightly hard"],
      ["way_too_hard", "Way too hard"],
    ];
    const rateBtns = ratings
      .map(([v, label]) => `<button class="btn btn-ghost btn-mini daily-rate ${daily.rating === v ? "chosen" : ""}" data-rate="${v}">${label}</button>`)
      .join("");
    const last = daily.qaIndex >= daily.qaQueue.length - 1;
    el.innerHTML = `
      <div class="daily-result-title">${title}</div>
      <div class="daily-result-line">🔵 ${daily.bluesFound}/9 · ✗ ${daily.mistakes} strikes · 💡 ${daily.hintsUsed} hints · ⏱ ${time}</div>
      ${answersHtml}
      <div class="daily-rate-label">How was the difficulty?</div>
      <div class="daily-rate-row">${rateBtns}</div>
      <textarea id="qa-note" class="qa-note" rows="3" placeholder="Notes for this board (bad clue, ambiguity, typo, too easy/hard…) — optional"></textarea>
      <div class="daily-result-btns">
        <button class="btn btn-primary" id="qa-next-btn">${last ? "Save &amp; finish batch" : "Save &amp; next board →"}</button>
        <button class="btn btn-ghost" id="qa-home-btn">Save &amp; exit</button>
      </div>`;
    $all(".daily-rate", el).forEach((b) => b.addEventListener("click", () => {
      daily.rating = b.dataset.rate;
      $all(".daily-rate", el).forEach((x) => x.classList.toggle("chosen", x.dataset.rate === daily.rating));
    }));
    $("#qa-next-btn").addEventListener("click", () => qaSaveAndAdvance());
    $("#qa-home-btn").addEventListener("click", async () => {
      await qaSaveAndAdvanceThenExit();
    });
    return;
  }

  // Tutorial finish: no score sharing, no difficulty rating, no caching —
  // just congratulate and point them at today's real puzzles.
  if (daily.practice) {
    const won = daily.outcome === "win";
    el.innerHTML = `
      <div class="daily-result-title">${won ? "Nice — you've got it! 🎉" : "Good try — that's the idea!"}</div>
      <div class="daily-result-line">That was just practice. Ready for today's puzzle?</div>
      ${answersHtml}
      <div class="daily-result-btns">
        <button class="btn btn-primary" id="daily-go-gen1">Play today's Gen I puzzle</button>
        <button class="btn btn-primary" id="daily-go-mixed">Play today's all-gens puzzle</button>
        <button class="btn btn-ghost" id="daily-home-btn">Home</button>
      </div>`;
    $("#daily-go-gen1").addEventListener("click", () => startDaily("gen1"));
    $("#daily-go-mixed").addEventListener("click", () => startDaily("mixed"));
    $("#daily-home-btn").addEventListener("click", () => { clearDailyUrl(); showScreen("landing"); });
    return;
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
  $("#daily-home-btn").addEventListener("click", () => { clearDailyUrl(); showScreen("landing"); });
  $all(".daily-rate", el).forEach((b) => b.addEventListener("click", () => dailyRate(b.dataset.rate)));
}

async function dailyRate(rating) {
  daily.rating = rating;
  renderDailyResult();
  _saveDailyProgress(); // remember the rating so it sticks on revisit
  if (daily.attemptId) {
    try { await sb.rpc("daily_rate_attempt", { p_id: daily.attemptId, p_rating: rating }); }
    catch (err) { console.error(err); }
  }
}

function dailyShare() {
  // No board grid – that would reveal the answers to whoever you share with
  // (change #3). Share only the outcome, mistakes, guesses and time.
  const time = fmtClock(dailyElapsedSecs());
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
  const url = dailyUrl(daily.pool); // links straight to this specific daily
  nativeShare({ title: "Pokémon Codenames – Daily", text, url });
}

// ============================================================================
// Boot
// ============================================================================
function goHome() {
  // Strip any ?code= so a refresh doesn't deep-join, hide the win overlay,
  // drop the room pill, and show the landing page. Session is left intact.
  try { history.replaceState(null, "", window.location.pathname); } catch {}
  const overlay = $("#win-overlay");
  if (overlay) overlay.classList.add("hidden");
  dailyPauseTimer(); // if leaving a daily mid-solve, bank the time
  setRoomPill(null);
  showScreen("landing");
}

async function boot() {
  initLandingScreen();
  initLobbyScreen();
  initGameScreen();
  initSoundToggle();
  initDaily();

  // Tapping the brand (logo + name) always returns to the homepage, from any
  // screen. Keeps the stored session so the game can be rejoined via its link.
  const brand = $("#brand-home");
  if (brand) {
    brand.addEventListener("click", goHome);
    brand.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); goHome(); }
    });
  }

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
    if (document.visibilityState === "visible") { resyncRoom(); dailyResumeTimer(); }
    else dailyPauseTimer(); // tab hidden / app backgrounded -> pause the daily timer
  });
  window.addEventListener("focus", () => { resyncRoom(); dailyResumeTimer(); });
  window.addEventListener("blur", () => dailyPauseTimer()); // clicked away -> pause
  setInterval(pollTick, POLL_MS);
  setInterval(() => {
    if (state.room && $("#screen-game").classList.contains("active")) renderTimer();
    if ($("#screen-daily").classList.contains("active") && daily.timerOn && !daily.finished) {
      const el = $("#daily-timer");
      if (el) el.textContent = fmtClock(dailyElapsedSecs());
    }
  }, 1000);

  _migrateOldSession(); // one-time migration from old single-session key

  // QA / playtest deep-link (unlisted): ?qa=1 plays upcoming boards back-to-back
  // with a feedback form after each, saved to daily_feedback.
  if (new URLSearchParams(window.location.search).get("qa") === "1") {
    await startQaBatch();
    return;
  }

  // Daily deep-link: ?daily=1 (Gen I) / ?daily=all (mixed) opens that puzzle.
  const dailyDeep = poolFromParam(new URLSearchParams(window.location.search).get("daily"));
  if (dailyDeep) {
    await startDaily(dailyDeep);
    return;
  }

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
