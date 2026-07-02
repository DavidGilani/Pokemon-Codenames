// ============================================================================
// Pokemon Codenames — app.js
// Shared Supabase setup, auth, realtime, and logic for all three screens
// (landing / lobby / game). This is plain JS, no build step — everything
// runs directly in the browser.
// ============================================================================

const SUPABASE_URL = "https://fjhijkszcugwxtmlbudz.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZqaGlqa3N6Y3Vnd3h0bWxidWR6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODMwMTExODcsImV4cCI6MjA5ODU4NzE4N30.MY29L3dGhgCAyrKS0bx0E30DbwiYHrb75dIzmjKBRZI";

const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const STORAGE_KEY = "pc_session";

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
  cardKey: null, // map position -> colour, only populated for spymasters
  channel: null,
  me: null, // players row for the current user
};

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
  if (code) {
    $("#room-pill-code").textContent = code;
    pill.classList.remove("hidden");
  } else {
    pill.classList.add("hidden");
  }
}

// ----------------------------------------------------------------------------
// Local persistence — just enough to survive a refresh
// ----------------------------------------------------------------------------
function saveSession() {
  localStorage.setItem(
    STORAGE_KEY,
    JSON.stringify({
      roomId: state.roomId,
      playerId: state.playerId,
      nickname: state.nickname,
    })
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
  if (state.channel) {
    sb.removeChannel(state.channel);
    state.channel = null;
  }
  setRoomPill(null);
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

// ============================================================================
// LANDING SCREEN
// ============================================================================

function initLandingScreen() {
  // Mode chips (online / in person)
  $all('input[name="mode"]').forEach((input) => {
    input.addEventListener("change", () => {
      $all(".radio-chip[data-role='mode']").forEach((chip) =>
        chip.classList.toggle("checked", chip.querySelector("input").checked)
      );
    });
  });

  // Generation chips — listen on the checkbox's own "change" event rather
  // than toggling manually on click, since a click on the wrapping label
  // already forwards a native click to the input (toggling it once on its
  // own); handling click too would double-toggle it back.
  $all(".gen-chip input").forEach((input) => {
    input.addEventListener("change", () => {
      input.closest(".gen-chip").classList.toggle("checked", input.checked);
    });
  });

  $("#create-room-form").addEventListener("submit", handleCreateRoom);
  $("#join-room-form").addEventListener("submit", handleJoinRoom);

  // If the URL carries a room code (shared link), pre-fill the join field
  const params = new URLSearchParams(window.location.search);
  const codeParam = params.get("code");
  if (codeParam) {
    $("#join-code").value = codeParam.toUpperCase();
  }
}

function collectSettings() {
  const generations = $all('.gen-chip input:checked').map((i) => Number(i.value));
  const wellKnownOnly = $("#well-known-toggle").checked;
  return {
    generations: generations.length ? generations : [1],
    well_known_only: wellKnownOnly,
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
    await enterLobby();
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
    const { data, error } = await sb.rpc("join_room", {
      p_code: code,
      p_nickname: nickname,
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
    errEl.textContent = err.message || "Couldn't join that room.";
  } finally {
    btn.disabled = false;
  }
}

// ============================================================================
// SHARED: fetching + realtime + routing between lobby/game
// ============================================================================

async function fetchRoom() {
  const { data, error } = await sb
    .from("rooms")
    .select("*")
    .eq("id", state.roomId)
    .single();
  if (error) throw error;
  state.room = data;
}

async function fetchPlayers() {
  // Not ordering by a timestamp here since the table's exact column set
  // (beyond what the RPC functions reference) isn't known — default
  // return order is fine for a small player list.
  const { data, error } = await sb
    .from("players")
    .select("*")
    .eq("room_id", state.roomId);
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
  state.cardKey = null;
  if (!state.me || state.me.role !== "spymaster") return;
  const { data, error } = await sb
    .from("card_key")
    .select("*")
    .eq("room_id", state.roomId);
  if (error) {
    // RLS may simply not allow this yet (e.g. game hasn't started) — fine
    return;
  }
  const map = {};
  (data || []).forEach((row) => (map[row.position] = row.colour));
  state.cardKey = map;
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
        render();
      }
    )
    .on(
      "postgres_changes",
      { event: "*", schema: "public", table: "players", filter: `room_id=eq.${state.roomId}` },
      async () => {
        await fetchPlayers();
        await fetchCardKeyIfSpymaster();
        render();
      }
    )
    .on(
      "postgres_changes",
      { event: "*", schema: "public", table: "cards", filter: `room_id=eq.${state.roomId}` },
      async (payload) => {
        await fetchCards();
        render(payload.new ? payload.new.position : null);
      }
    )
    .subscribe((status) => {
      if (status === "SUBSCRIBED") {
        // Freshly (re)connected — pull the latest state in case anything
        // changed while we were disconnected, then clear any pending retry.
        if (reconnectTimer) {
          clearTimeout(reconnectTimer);
          reconnectTimer = null;
        }
        resyncRoom();
      } else if (status === "CHANNEL_ERROR" || status === "TIMED_OUT" || status === "CLOSED") {
        // The websocket dropped (common on mobile networks / backgrounded
        // tabs). Retry after a short delay rather than leaving the client
        // silently stale until the person manually refreshes.
        if (!reconnectTimer && state.roomId) {
          reconnectTimer = setTimeout(() => {
            reconnectTimer = null;
            subscribeToRoom();
          }, 2000);
        }
      }
    });
}

// Re-fetch everything for the current room and re-render. Used whenever we
// regain a realtime connection or the tab becomes visible again, so a
// missed update never leaves the screen stale.
async function resyncRoom() {
  if (!state.roomId) return;
  try {
    await fetchRoom();
    await fetchPlayers();
    if (state.room && state.room.status !== "lobby") {
      await fetchCards();
    }
    await fetchCardKeyIfSpymaster();
    render();
  } catch (err) {
    console.error("Resync failed:", err);
  }
}

async function enterRoom() {
  await fetchRoom();
  await fetchPlayers();
  if (!state.me) {
    // Room or player vanished — start over
    clearSession();
    showScreen("landing");
    return;
  }
  subscribeToRoom();
  if (state.room.status === "lobby") {
    await enterLobby();
  } else {
    await enterGame();
  }
}

async function enterLobby() {
  await fetchRoom();
  await fetchPlayers();
  setRoomPill(state.room.code);
  renderLobby();
  showScreen("lobby");
}

async function enterGame() {
  await fetchRoom();
  await fetchPlayers();
  await fetchCards();
  await fetchCardKeyIfSpymaster();
  setRoomPill(state.room.code);
  renderGame();
  showScreen("game");
}

async function render(changedPosition) {
  if (!state.room) return;

  if (state.room.status === "lobby") {
    renderLobby();
    showScreen("lobby");
    return;
  }

  // First time we see the room leave the lobby (e.g. the host just dealt
  // the board), we won't have cards or the key loaded yet — fetch once.
  if (state.cards.length === 0) {
    await fetchCards();
    await fetchCardKeyIfSpymaster();
  }
  renderGame(changedPosition);
  showScreen("game");
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
      <button class="btn btn-ghost" data-action="claim" data-team="${team}" data-role="operative">Join as operative</button>
      <button class="btn btn-ghost" data-action="claim" data-team="${team}" data-role="spymaster">Be spymaster</button>
    </div>`;
}

function renderTeamColumn(team) {
  const col = $(`#team-${team}-list`);
  const teamPlayers = state.players.filter((p) => p.team === team);
  const spymaster = teamPlayers.find((p) => p.role === "spymaster");
  const operatives = teamPlayers.filter((p) => p.role === "operative");

  let html = `<div class="role-slot">Spymaster</div>`;
  html += spymaster
    ? playerChipHtml(spymaster)
    : `<div class="empty-slot">Open seat</div>`;

  html += `<div class="role-slot">Operatives</div>`;
  html += operatives.length
    ? operatives.map(playerChipHtml).join("")
    : `<div class="empty-slot">No operatives yet</div>`;

  col.innerHTML = html;
}

function playerChipHtml(p) {
  return `<div class="player-chip"><span>${escapeHtml(p.nickname)}</span>${
    p.is_host ? `<span class="host-badge">HOST</span>` : ""
  }</div>`;
}

function renderLobby() {
  if (!state.room) return;
  $("#lobby-room-code").textContent = state.room.code;
  renderTeamColumn("red");
  renderTeamColumn("blue");

  const seatArea = $("#seat-picker");
  if (state.me && state.me.team) {
    seatArea.innerHTML = `<div class="waiting-note">You're set as <strong>${state.me.role}</strong> on <strong>${state.me.team}</strong>. Waiting for the host to start the game.</div>`;
  } else {
    seatArea.innerHTML = `
      <div class="team-col team-red">${seatButtonsHtml("red")}</div>
      <div class="team-col team-blue">${seatButtonsHtml("blue")}</div>
    `;
    seatArea.classList.add("teams-grid");
  }

  $all('[data-action="claim"]', seatArea).forEach((btn) => {
    btn.addEventListener("click", () => handleClaimSeat(btn.dataset.team, btn.dataset.role));
  });

  const hostPanel = $("#host-panel");
  const isHost = state.me && state.me.is_host;
  hostPanel.classList.toggle("hidden", !isHost);
  if (isHost) {
    const redReady = state.players.some((p) => p.team === "red" && p.role === "spymaster");
    const blueReady = state.players.some((p) => p.team === "blue" && p.role === "spymaster");
    const ready = redReady && blueReady;
    $("#start-game-btn").disabled = !ready;
    $("#start-game-hint").textContent = ready
      ? "Both teams have a spymaster — ready to deal."
      : "Each team needs a spymaster before you can start.";
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
    await fetchPlayers();
    renderLobby();
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't claim that seat.");
  }
}

async function handleStartGame() {
  const btn = $("#start-game-btn");
  btn.disabled = true;
  try {
    const { error } = await sb.rpc("start_game", { p_room_id: state.roomId });
    if (error) throw error;
    await enterGame();
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
  $("#end-turn-btn").addEventListener("click", handleEndTurn);
  $("#leave-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
  $("#new-game-btn").addEventListener("click", () => {
    clearSession();
    showScreen("landing");
  });
}

function otherTeam(team) {
  return team === "red" ? "blue" : "red";
}

function canReveal() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress") return false;
  if (!room.current_clue) return false;
  if (room.mode === "online") {
    return me.team === room.current_team && me.role === "operative";
  }
  return me.is_host || me.team === room.current_team;
}

function canPass() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || !room.current_clue) return false;
  return me.is_host || me.team === room.current_team;
}

function canGiveClue() {
  const room = state.room;
  const me = state.me;
  if (!room || !me) return false;
  if (room.status !== "in_progress" || room.current_clue) return false;
  return me.role === "spymaster" && me.team === room.current_team;
}

function renderGame(changedPosition) {
  const room = state.room;
  if (!room) return;

  // Turn banner
  const banner = $("#turn-banner");
  banner.classList.remove("team-red", "team-blue");
  if (room.status === "in_progress") {
    banner.classList.add(`team-${room.current_team}`);
    $("#turn-team-value").textContent = `${room.current_team.toUpperCase()} TEAM'S TURN`;
  } else {
    $("#turn-team-value").textContent = room.status === "finished" ? "Game over" : "—";
  }

  const clueReadout = $("#clue-readout");
  if (room.current_clue) {
    clueReadout.classList.remove("hidden");
    $("#clue-word-value").textContent = room.current_clue.word;
    $("#clue-count-value").textContent = `${room.guesses_remaining} guess${
      room.guesses_remaining === 1 ? "" : "es"
    } left`;
  } else {
    clueReadout.classList.add("hidden");
  }

  // Mode / role banner for spymasters
  const spyBanner = $("#spy-banner");
  if (state.me && state.me.role === "spymaster") {
    spyBanner.classList.remove("hidden");
    spyBanner.textContent = "Spymaster view — only you can see the key";
  } else {
    spyBanner.classList.add("hidden");
  }

  // Clue form
  const clueForm = $("#clue-form");
  if (canGiveClue()) {
    clueForm.classList.remove("hidden");
  } else {
    clueForm.classList.add("hidden");
  }
  const waitingForClue = $("#waiting-for-clue");
  if (room.status === "in_progress" && !room.current_clue && !canGiveClue()) {
    waitingForClue.classList.remove("hidden");
    waitingForClue.textContent = `Waiting for the ${room.current_team} spymaster's clue...`;
  } else {
    waitingForClue.classList.add("hidden");
  }

  // End turn button
  $("#end-turn-btn").classList.toggle("hidden", !canPass());

  // Board
  renderBoard(changedPosition);

  // Tile counts
  const redLeft = countRemaining(room, "red");
  const blueLeft = countRemaining(room, "blue");
  $("#count-red").textContent = redLeft === null ? "—" : redLeft;
  $("#count-blue").textContent = blueLeft === null ? "—" : blueLeft;

  // Win overlay
  const winOverlay = $("#win-overlay");
  if (room.status === "finished") {
    winOverlay.classList.remove("hidden");
    const card = $("#win-card");
    card.classList.remove("win-red", "win-blue");
    card.classList.add(`win-${room.winner}`);
    $("#win-title").textContent = `${room.winner.toUpperCase()} TEAM WINS`;
  } else {
    winOverlay.classList.add("hidden");
  }
}

function countRemaining(room, team) {
  // Total per team is knowable to everyone (9 for the starting team, 8 for
  // the other) without needing the hidden key, same as the physical game's
  // count-tracker — this works for operatives too, not just spymasters.
  if (!room.starting_team) return null;
  const total = team === room.starting_team ? 9 : 8;
  const revealed = state.cards.filter(
    (c) => c.revealed && c.revealed_colour === team
  ).length;
  return total - revealed;
}

function renderBoard(changedPosition) {
  const board = $("#board");
  board.innerHTML = "";
  const allowClick = canReveal();
  const peekLabel = { red: "R", blue: "B", neutral: "N", assassin: "A" };

  state.cards.forEach((card) => {
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

    if (!revealed && !allowClick) tile.classList.add("locked");
    if (card.position === changedPosition && revealed) tile.classList.add("scan-sweep");

    const badgeHtml = peekColour
      ? `<div class="peek-badge">${peekLabel[peekColour]}</div>`
      : "";

    tile.innerHTML = `
      ${badgeHtml}
      <div class="tile-img-wrap"><img src="${card.sprite_url}" alt="${escapeHtml(card.name)}" loading="lazy" /></div>
      <div class="tile-name">${escapeHtml(card.name)}</div>
    `;

    if (!revealed && allowClick) {
      tile.addEventListener("click", () => handleRevealCard(card.position));
    }

    board.appendChild(tile);
  });
}

async function handleSubmitClue(e) {
  e.preventDefault();
  const word = $("#clue-word").value.trim();
  const number = Number($("#clue-number").value);
  if (!word) return;
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
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't submit that clue.");
  } finally {
    btn.disabled = false;
  }
}

async function handleRevealCard(position) {
  try {
    const { error } = await sb.rpc("reveal_card", {
      p_room_id: state.roomId,
      p_position: position,
    });
    if (error) throw error;
  } catch (err) {
    console.error(err);
    toast(err.message || "Couldn't reveal that tile.");
  }
}

async function handleEndTurn() {
  try {
    const { error } = await sb.rpc("end_turn", { p_room_id: state.roomId });
    if (error) throw error;
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

  await ensureAuth();

  // Backstop for flaky mobile connections: whenever the tab regains focus
  // or becomes visible again, pull fresh state. Realtime's own reconnect
  // (above) should usually cover this, but this catches anything it misses.
  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") resyncRoom();
  });
  window.addEventListener("focus", () => resyncRoom());

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
  showScreen("landing");
}

boot();
