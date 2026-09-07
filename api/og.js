// Dynamic Open Graph image for the daily puzzle link preview.
// Crawlers (WhatsApp, iMessage, Twitter/X, Facebook, Slack…) don't run JS, so a
// per-day preview has to be produced server-side. This edge function renders a
// PNG card showing today's clues + the brand mark. It is SPOILER-SAFE: it only
// uses get_daily_puzzle, which strips the hidden tile targets, so the answers
// are never exposed – only the clue words the player would see anyway.
//
//   /api/og?daily=1    -> Gen I     /api/og?daily=all -> All-gens
//
import { ImageResponse } from "@vercel/og";

export const config = { runtime: "edge" };

const SUPABASE_URL = "https://fjhijkszcugwxtmlbudz.supabase.co";
const ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZqaGlqa3N6Y3Vnd3h0bWxidWR6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODMwMTExODcsImV4cCI6MjA5ODU4NzE4N30.MY29L3dGhgCAyrKS0bx0E30DbwiYHrb75dIzmjKBRZI";

const LOGO_DATA_URI = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxODAgMTgwIj4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0iciIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iI2ZmNWI1MiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2RmM2IzMiIvPjwvbGluZWFyR3JhZGllbnQ+CjxsaW5lYXJHcmFkaWVudCBpZD0idyIgeDE9IjAiIHkxPSIwIiB4Mj0iMCIgeTI9IjEiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iI2ZmZiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2U2ZThlZSIvPjwvbGluZWFyR3JhZGllbnQ+CjxyYWRpYWxHcmFkaWVudCBpZD0ibCIgY3g9IjAuMzUiIGN5PSIwLjMyIiByPSIwLjgiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iI2JmZTRmZiIgc3RvcC1vcGFjaXR5PSIwLjU1Ii8+PHN0b3Agb2Zmc2V0PSIwLjU1IiBzdG9wLWNvbG9yPSIjN2ZiNGU2IiBzdG9wLW9wYWNpdHk9IjAuMTgiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMzZDZlYTUiIHN0b3Atb3BhY2l0eT0iMC4zMCIvPjwvcmFkaWFsR3JhZGllbnQ+CjwvZGVmcz4KPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODQgOTYpIj4KPGNpcmNsZSByPSI1OCIgZmlsbD0idXJsKCN3KSIgc3Ryb2tlPSIjMTIxNTFmIiBzdHJva2Utd2lkdGg9IjYiLz4KPHBhdGggZD0iTS01OCAwYTU4IDU4IDAgMCAxIDExNiAwWiIgZmlsbD0idXJsKCNyKSIvPgo8cmVjdCB4PSItNTgiIHk9Ii01LjUiIHdpZHRoPSIxMTYiIGhlaWdodD0iMTEiIGZpbGw9IiMxMjE1MWYiLz4KPGNpcmNsZSByPSIxOSIgZmlsbD0iI2Y0ZjZmYiIgc3Ryb2tlPSIjMTIxNTFmIiBzdHJva2Utd2lkdGg9IjYiLz4KPGNpcmNsZSByPSI4LjUiIGZpbGw9IiNmZmYiIHN0cm9rZT0iIzEyMTUxZiIgc3Ryb2tlLXdpZHRoPSI0Ii8+CjxlbGxpcHNlIGN4PSItMjIiIGN5PSItMzAiIHJ4PSIxOCIgcnk9IjEwIiBmaWxsPSIjZmZmIiBvcGFjaXR5PSIwLjI4Ii8+CjwvZz4KPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNjAgNDApIHJvdGF0ZSgtMTYpIj4KPGVsbGlwc2UgY3g9IjAiIGN5PSIxNCIgcng9IjQwIiByeT0iOSIgZmlsbD0iIzIwMjQyZSIvPgo8cGF0aCBkPSJNLTI0IDE0YzAtMjAgNC0zMCAyNC0zMHMyNCAxMCAyNCAzMFoiIGZpbGw9IiMyYjMwNDAiLz4KPHJlY3QgeD0iLTI0IiB5PSI5IiB3aWR0aD0iNDgiIGhlaWdodD0iNyIgcng9IjMuNSIgZmlsbD0iIzE2MWEyNCIvPgo8L2c+CjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEyOCAxMzIpIHJvdGF0ZSgyMCkiPgo8bGluZSB4MT0iOCIgeTE9IjgiIHgyPSIzNCIgeTI9IjM0IiBzdHJva2U9IiMxMjE1MWYiIHN0cm9rZS13aWR0aD0iMTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8bGluZSB4MT0iOCIgeTE9IjgiIHgyPSIzNCIgeTI9IjM0IiBzdHJva2U9IiNjOWEyNGEiIHN0cm9rZS13aWR0aD0iNyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CjxjaXJjbGUgcj0iMjQiIGZpbGw9InVybCgjbCkiIHN0cm9rZT0iIzEyMTUxZiIgc3Ryb2tlLXdpZHRoPSIxMCIvPgo8Y2lyY2xlIHI9IjI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNlNmM3NjYiIHN0cm9rZS13aWR0aD0iNC41Ii8+CjxwYXRoIGQ9Ik0tMTIgLTZhMTggMTggMCAwIDEgMTIgLTExIiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmYiIHN0cm9rZS13aWR0aD0iNCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBvcGFjaXR5PSIwLjc1Ii8+CjwvZz4KPC9zdmc+Cg==";

function difficulty(clues) {
  const cats = (clues || []).map((c) => c.cat || 1);
  const ones = cats.filter((c) => c === 1).length;
  const highs = cats.filter((c) => c >= 4).length;
  if (highs >= 4) return "Evil";
  if (highs >= 3) return "Brutal";
  if (ones === 0) return "Hard";
  if (ones === 1) return "Challenging";
  if (ones === 2) return "Medium";
  return "Easy";
}
const MO = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
function ordinal(n){ const s=["th","st","nd","rd"], v=n%100; return n+(s[(v-20)%10]||s[v]||s[0]); }
function dateLabel(iso){
  const d = new Date(iso + "T00:00:00Z");
  if (isNaN(d)) return "";
  return `${MO[d.getUTCMonth()]} ${ordinal(d.getUTCDate())} ${d.getUTCFullYear()}`;
}
// tiny element helper so we don't need JSX / a build step. 4th arg carries any
// non-style props (e.g. an <img> src), which Satori reads directly.
const h = (type, style, children, props = {}) => ({ type, props: { style, children, ...props } });

export default async function handler(req) {
  const url = new URL(req.url);
  const p = url.searchParams.get("daily") === "all" ? "all" : "1";
  const pool = p === "all" ? "mixed" : "gen1";
  const poolLabel = pool === "gen1" ? "Gen I" : "All-gens";

  let clues = [], date = "";
  try {
    const r = await fetch(`${SUPABASE_URL}/rest/v1/rpc/get_daily_puzzle`, {
      method: "POST",
      headers: { apikey: ANON_KEY, authorization: `Bearer ${ANON_KEY}`, "content-type": "application/json" },
      body: JSON.stringify({ p_pool: pool }),
    });
    const rows = await r.json();
    const row = Array.isArray(rows) ? rows[0] : rows;
    if (row) { clues = row.clues || []; date = row.puzzle_date || ""; }
  } catch (_) { /* fall through to a clue-less card */ }

  const diff = difficulty(clues);
  const [bold, regular] = await Promise.all([
    fetch(new URL("/ogassets/Outfit-Bold.ttf", url.origin)).then((r) => r.arrayBuffer()),
    fetch(new URL("/ogassets/Outfit-Regular.ttf", url.origin)).then((r) => r.arrayBuffer()),
  ]);

  const chip = (c) => h("div", {
    display: "flex", alignItems: "center", background: "#1b2130",
    border: "1px solid #2b3346", borderRadius: 12, padding: "10px 16px", margin: 6,
    fontSize: 30, color: "#eef1f8", fontWeight: 700,
  }, [
    String(c.word || ""),
    h("span", { color: "#8b95ad", fontWeight: 400, marginLeft: 10, fontSize: 26 },
      c.anti ? "×0" : `×${c.number || 1}`),
  ]);

  const tree = h("div", {
    width: "100%", height: "100%", display: "flex", flexDirection: "column",
    background: "linear-gradient(160deg,#1b2030,#0e1119)", padding: 56,
    fontFamily: "Outfit", color: "#eef1f8",
  }, [
    // header row: logo + wordmark
    h("div", { display: "flex", alignItems: "center", marginBottom: 8 }, [
      h("img", { width: 92, height: 92, marginRight: 22 }, [], { src: LOGO_DATA_URI, width: 92, height: 92 }),
      h("div", { display: "flex", flexDirection: "column" }, [
        h("div", { fontSize: 52, fontWeight: 700, lineHeight: 1.05 }, "Pokémon Codenames"),
        h("div", { fontSize: 30, color: "#9aa4bd", marginTop: 6 },
          `Daily · ${poolLabel} · ${diff}${date ? " · " + dateLabel(date) : ""}`),
      ]),
    ]),
    // clues
    h("div", { fontSize: 26, color: "#c9a24a", fontWeight: 700, letterSpacing: 2,
      textTransform: "uppercase", margin: "26px 0 6px" }, "Today's clues"),
    h("div", { display: "flex", flexWrap: "wrap", alignContent: "flex-start", flex: 1 },
      (clues.length ? clues : [{ word: "Play today's puzzle", number: 9 }]).slice(0, 6).map(chip)),
    // footer
    h("div", { display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 8 }, [
      h("div", { fontSize: 30, fontWeight: 700, color: "#ffd24a" }, "Can you solve it?"),
      h("div", { fontSize: 26, color: "#78829e" }, (url.host || "")),
    ]),
  ]);

  return new ImageResponse(tree, {
    width: 1200, height: 630,
    fonts: [
      { name: "Outfit", data: bold, weight: 700, style: "normal" },
      { name: "Outfit", data: regular, weight: 400, style: "normal" },
    ],
    headers: { "cache-control": "public, max-age=1800, s-maxage=1800" },
  });
}
