// ============================================================================
// Pokemon Codenames — app.js
// Shared Supabase setup, auth, realtime, and logic for all three screens
// (landing / lobby / game). Plain JS, no build step — runs in the browser.
// ============================================================================

const SUPABASE_URL = "https://fjhijkszcugwxtmlbudz.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZqaGlqa3N6Y3Vnd3h0bWxidWR6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODMwMTExODcsImV4cCI6MjA5ODU4NzE4N30.MY29L3dGhgCAyrKS0bx0E30DbwiYHrb75dIzmjKBRZI";

const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const STORAGE_KEY = "pc_session";
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
};

let lastSignature = null;   // used by the poll to avoid needless re-renders
let statsRequested = false; // record the two-player result only once
let serverOffsetMs = 0;     // (server clock) - (this device's clock)

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
// Local persistence — just enough to survive a refresh
// ----------------------------------------------------------------------------
function saveSession() {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({ roomId: state.roomId, playerId: state.playerId, nickname: state.nickname })
  );
}

function loadSession() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
  } catch {
    return null;
  }
}

function clearSession() {
  localStorage.removeItem(STORAGE_KEY);
  state.roomId = null;
  state.playerId = null;
  state.room = null;
  state.players = [];
  state.cards = [];
  state.cardKey = null;
  state.me = null;
  state.turnStartRevealed = new Set();
  state.lastClueWord = null;
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
// Auth — anonymous sign-in, persisted by supabase-js itself
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
      errEl.textContent = err.message || "Couldn't join — check the link and try again.";
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
async function resyncRoom() {
  if (!state.roomId) return;
  try {
    await fetchRoom();
    await fetchPlayers();
    await fetchCards();
    await fetchCardKeyIfSpymaster();
    await render();
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
    /* transient — next tick retries */
  }
}

async function enterRoom() {
  await fetchRoom();
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
}

// ----------------------------------------------------------------------------
// Rendering — single entry point that routes to lobby or game
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
function makeTile(card, { interactive, changedPosition }) {
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
  if (changedPosition != null && card.position === changedPosition && revealed) {
    tile.classList.add("scan-sweep");
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
  if (el.dataset.sig === sig) return;
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
  $("#lobby-room-code").textContent = room.code;

  // Mode instructions
  const info = $("#lobby-info");
  if (room.mode === "in_person") {
    info.classList.remove("hidden");
    info.innerHTML = `<strong>In-person mode.</strong> Share this screen so everyone can see the board. Each clue giver should join separately on their own phone using the room code, so they can privately see which Pokémon belong to their team. Everyone else can watch and call out guesses from this shared screen.`;
  } else if (is2p) {
    info.classList.remove("hidden");
    info.innerHTML = `<strong>Two-player mode.</strong> One of you is the clue giver, the other the clue receiver. Work together to reveal all of your team's Pokémon in as few rounds as possible — and never touch the assassin.`;
  } else {
    info.classList.add("hidden");
  }

  // Board preview (no colours unless you've claimed clue giver)
  renderBoardInto($("#lobby-board"), { interactive: false });

  // Team columns
  const redCol = $("#lobby-red-col");
  const blueCol = $("#lobby-blue-col");
  if (is2p) {
    redCol.classList.add("hidden");
    blueCol.classList.remove("hidden");
    $("#lobby-blue-title").textContent = "Players";
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
    const teamLabel = is2p ? "" : ` on <strong>${state.me.team}</strong>`;
    seatArea.className = "";
    seatArea.innerHTML = `<div class="waiting-note">You're set as <strong>${roleLabel}</strong>${teamLabel}. Waiting for the host to start.</div>`;
  } else if (is2p) {
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

  // Host controls
  const hostPanel = $("#host-panel");
  const isHost = state.me && state.me.is_host;
  hostPanel.classList.toggle("hidden", !isHost);
  if (isHost) {
    let ready, hint;
    if (is2p) {
      const hasGiver = state.players.some((p) => p.role === "spymaster" && p.team);
      const hasReceiver = state.players.some((p) => p.role === "operative" && p.team);
      ready = hasGiver && hasReceiver;
      hint = ready ? "Ready to start." : "Need a clue giver and a clue receiver.";
    } else {
      const redReady = state.players.some((p) => p.team === "red" && p.role === "spymaster");
      const blueReady = state.players.some((p) => p.team === "blue" && p.role === "spymaster");
      ready = redReady && blueReady;
      hint = ready
        ? "Both teams have a clue giver — ready to start."
        : "Each team needs a clue giver before you can start.";
    }
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
  $("#share-clue-btn").addEventListener("click", handleShareClue);
  $("#share-board-btn").addEventListener("click", handleShareBoard);
  $("#leave-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
  $("#new-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
  $("#see-board-btn").addEventListener("click", () => {
    $("#win-overlay").classList.add("hidden");
  });
}

function isTwoPlayer(room) {
  return room?.mode === "two_player" || room?.mode === "turn_by_turn";
}

function isAsyncMode(room) {
  return room?.mode === "turn_by_turn";
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
  if (isTwoPlayer(room)) return me.role === "operative";
  return me.team === room.current_team && me.role === "operative";
}

function canPass() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || !room.current_clue) return false;
  if (room.mode === "in_person") return me.is_host || me.team === room.current_team;
  if (isTwoPlayer(room)) return me.role === "operative";
  return me.team === room.current_team && me.role === "operative";
}

function canGiveClue() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || room.current_clue) return false;
  if (isTwoPlayer(room)) return me.role === "spymaster";
  return me.role === "spymaster" && me.team === room.current_team;
}

function renderGame(changedPosition) {
  const room = state.room;
  if (!room) return;
  const is2p = isTwoPlayer(room);
  const isAsync = isAsyncMode(room);

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
    $("#turn-team-value").textContent = is2p
      ? room.current_clue ? "GUESSING" : "CLUE GIVER'S TURN"
      : `${room.current_team.toUpperCase()} TEAM'S TURN`;
  } else {
    $("#turn-team-value").textContent = room.status === "finished" ? "Game over" : "—";
  }

  // Timer
  renderTimer();

  // Clue readout (word + number)
  const clueReadout = $("#clue-readout");
  if (room.current_clue) {
    clueReadout.classList.remove("hidden");
    $("#clue-word-value").textContent = `${room.current_clue.word}, ${room.current_clue.number}`;
    $("#clue-count-value").textContent = `${room.guesses_remaining} guess${
      room.guesses_remaining === 1 ? "" : "es"
    } left`;
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
  spyBanner.classList.toggle("hidden", !isGiver);
  observerBanner.classList.toggle("hidden", !observer);
  if (isGiver) spyBanner.textContent = "Clue giver view — only you can see the key";
  const legend = $("#board-legend");
  legend.classList.toggle("hidden", !isGiver);
  $("#legend-red").classList.toggle("hidden", is2p); // no red team in two-player

  // Clue form
  $("#clue-form").classList.toggle("hidden", !canGiveClue());

  // Waiting-for-clue line
  const waiting = $("#waiting-for-clue");
  if (room.status === "in_progress" && !room.current_clue && !canGiveClue()) {
    waiting.classList.remove("hidden");
    waiting.textContent = is2p
      ? "Waiting for the clue giver's clue..."
      : `Waiting for the ${room.current_team} clue giver's clue...`;
  } else {
    waiting.classList.add("hidden");
  }

  // End turn button
  $("#end-turn-btn").classList.toggle("hidden", !canPass());

  // Share clue — only for the clue giver, and only while a clue is active
  const isSpymaster = state.me?.role === "spymaster";
  const hasClue = room.status === "in_progress" && !!room.current_clue;
  $("#share-clue-row").classList.toggle("hidden", !(isSpymaster && hasClue));

  // Share board — only for operatives (clue receivers), only between turns (no active clue)
  const isOperative = state.me?.role === "operative";
  const betweenTurns = room.status === "in_progress" && !room.current_clue;
  $("#share-board-row").classList.toggle("hidden", !(isOperative && betweenTurns));

  // Board
  renderBoardInto($("#board"), { interactive: true, changedPosition });

  // In-game team roster (always visible so players know who's who)
  renderGameTeams(room);

  // Clue log
  renderClueLog(room);

  // Counts / rounds
  const redLeft = countRemaining(room, "red");
  const blueLeft = countRemaining(room, "blue");
  if (is2p) {
    $("#count-red-wrap").classList.add("hidden");
    $("#count-blue-wrap").classList.remove("hidden");
    $("#count-blue").textContent = blueLeft === null ? "—" : blueLeft;
    $("#round-wrap").classList.remove("hidden");
    $("#round-count").textContent = room.clue_count ?? 0;
  } else {
    $("#count-red-wrap").classList.remove("hidden");
    $("#count-blue-wrap").classList.remove("hidden");
    $("#round-wrap").classList.add("hidden");
    $("#count-red").textContent = redLeft === null ? "—" : redLeft;
    $("#count-blue").textContent = blueLeft === null ? "—" : blueLeft;
  }

  // Win / lose overlay
  const winOverlay = $("#win-overlay");
  if (room.status === "finished") {
    winOverlay.classList.remove("hidden");
    const card = $("#win-card");
    card.classList.remove("win-red", "win-blue");
    if (is2p) {
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
        $("#win-subtitle").textContent = "The assassin got you — better luck next time.";
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

  const is2p = isTwoPlayer(room);
  const isAsync = isAsyncMode(room);

  if (room.status === "in_progress") {
    if (is2p) {
      const start = room.started_at ? new Date(room.started_at).getTime() : serverNow();
      el.textContent = `Time elapsed: ${formatDuration(serverNow() - start, isAsync)}`;
    } else {
      const start = room.turn_started_at ? new Date(room.turn_started_at).getTime() : serverNow();
      el.textContent = `This turn: ${formatDuration(serverNow() - start)}`;
    }
  } else if (room.status === "finished" && is2p) {
    const start = room.started_at ? new Date(room.started_at).getTime() : 0;
    const end = room.finished_at ? new Date(room.finished_at).getTime() : serverNow();
    el.textContent = `Total time: ${formatDuration(end - start, isAsync)}`;
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

  const playerRow = (p) => {
    const roleLabel = p.role === "spymaster" ? "clue giver" : p.role === "operative" ? "receiver" : "";
    const meTag = p.id === state.playerId ? " (you)" : "";
    return `<div class="gt-player"><span>${escapeHtml(p.nickname)}${escapeHtml(meTag)}</span>${
      roleLabel ? `<span class="gt-role">${roleLabel}</span>` : ""
    }</div>`;
  };

  if (is2p) {
    const bluePlayers = state.players.filter((p) => p.team === "blue");
    if (bluePlayers.length === 0) { el.classList.add("hidden"); return; }
    el.classList.remove("hidden");
    el.innerHTML = `<div class="gt-col gt-single"><div class="gt-title">Players</div>${bluePlayers.map(playerRow).join("")}</div>`;
  } else {
    const red = state.players.filter((p) => p.team === "red");
    const blue = state.players.filter((p) => p.team === "blue");
    if (red.length === 0 && blue.length === 0) { el.classList.add("hidden"); return; }
    el.classList.remove("hidden");
    el.innerHTML = `
      <div class="gt-col gt-red"><div class="gt-title">Red team</div>${red.length ? red.map(playerRow).join("") : '<div class="gt-player" style="color:var(--text-faint)">—</div>'}</div>
      <div class="gt-col gt-blue"><div class="gt-title">Blue team</div>${blue.length ? blue.map(playerRow).join("") : '<div class="gt-player" style="color:var(--text-faint)">—</div>'}</div>`;
  }
}

// ----------------------------------------------------------------------------
// Clue log
// ----------------------------------------------------------------------------
function renderClueLog(room) {
  const panel = $("#clue-log");
  const list = $("#clue-log-list");
  const log = Array.isArray(room.clue_log) ? room.clue_log : [];
  if (log.length === 0) {
    panel.classList.add("hidden");
    return;
  }
  panel.classList.remove("hidden");
  list.innerHTML = log
    .map((c) => {
      const teamClass = c.team === "red" ? "cl-red" : "cl-blue";
      return `<div class="clue-log-row"><span class="cl-dot ${teamClass}"></span><span class="cl-word">${escapeHtml(
        c.word
      )}</span><span class="cl-num">${c.number}</span></div>`;
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
        : `<br>You're the first to finish — a record to beat!`;
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

async function handleShareClue() {
  const clue = state.room?.current_clue;
  if (!clue) return;
  const url = roomUrl();
  const room = state.room;
  const remaining = room?.remaining_blue;
  const grid = buildEmojiGrid();
  const remainLine = remaining != null ? `${remaining} blue tile${remaining === 1 ? "" : "s"} left to find` : "";
  const text = [
    `Pokémon Codenames`,
    `Clue: ${clue.word} × ${clue.number}`,
    grid,
    remainLine,
    `Your turn:`,
  ].filter(Boolean).join("\n");
  await nativeShare({ title: "Pokémon Codenames — clue", text, url });
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

async function handleShareBoard() {
  const url = roomUrl();
  const room = state.room;
  const is2p = isTwoPlayer(room);
  const myTeam = is2p ? "blue" : state.me?.team;

  // Work out what was guessed this turn using the snapshot taken when the clue arrived
  const thisRoundCards = state.cards.filter((c) => c.revealed && !state.turnStartRevealed.has(c.position));
  const correct = thisRoundCards.filter((c) => c.revealed_colour === myTeam).length;
  const wrong = thisRoundCards.filter((c) => c.revealed_colour !== myTeam).length;

  // Remaining team tiles — read from room columns, visible to everyone
  const remaining = is2p ? room.remaining_blue : (myTeam === "red" ? room.remaining_red : room.remaining_blue);

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

  await nativeShare({ title: "Pokémon Codenames — board update", text, url });
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
    $("#clue-word").value = "";
    $("#clue-number").value = "1";
    await resyncRoom();
    if (isAsyncMode(state.room)) await handleShareClue();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't submit that clue.");
  } finally {
    btn.disabled = false;
  }
}

async function handleRevealCard(position) {
  try {
    const { error } = await sb.rpc("reveal_card", { p_room_id: state.roomId, p_position: position });
    if (error) throw error;
    await resyncRoom();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't reveal that tile.");
  }
}

async function handleEndTurn() {
  try {
    const { error } = await sb.rpc("end_turn", { p_room_id: state.roomId });
    if (error) throw error;
    await resyncRoom();
    if (isAsyncMode(state.room)) await handleShareBoard();
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
// Boot
// ============================================================================
async function boot() {
  initLandingScreen();
  initLobbyScreen();
  initGameScreen();

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
  }, 1000);

  const saved = loadSession();
  if (saved && saved.roomId && saved.playerId) {
    state.roomId = saved.roomId;
    state.playerId = saved.playerId;
    state.nickname = saved.nickname || "";
    try {
      await enterRoom();
      return;
    } catch (err) {
      console.error(err);
      clearSession();
    }
  }

  // If arriving via a ?code= invite link (and no live session), show the quick-join overlay
  const inviteCode = new URLSearchParams(window.location.search).get("code");
  if (inviteCode) {
    const el = $("#quick-join-code");
    el.textContent = inviteCode.toUpperCase();
    el.dataset.code = inviteCode.toUpperCase();
    $("#quick-join-overlay").classList.remove("hidden");
    return;
  }

  showScreen("landing");
}

boot();
