// Per-day link-preview shim for the daily puzzle. A shared link like /d/1 hits
// this (via the vercel.json rewrite). Crawlers read the Open Graph tags below –
// which point og:image at the dynamic /api/og card – while real browsers are
// bounced straight into the SPA at /?daily=… so play is unaffected.
export const config = { runtime: "edge" };

export default function handler(req) {
  const url = new URL(req.url);
  const p = url.searchParams.get("daily") === "all" ? "all" : "1";
  const pool = p === "all" ? "mixed" : "gen1";
  const poolLabel = pool === "gen1" ? "Gen I" : "All-gens";
  const origin = url.origin;
  const img = `${origin}/api/og?daily=${p}`;
  const target = `${origin}/?daily=${p}`;
  const esc = (s) => String(s).replace(/[&<>"]/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]));
  const title = `Pokémon Codenames – Daily (${poolLabel})`;
  const desc = "Crack today's board from a handful of one-word clues – can you find all 9 hidden Pokémon?";
  const html = `<!doctype html><html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="${esc(img)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta property="og:url" content="${esc(target)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(title)}">
<meta name="twitter:description" content="${esc(desc)}">
<meta name="twitter:image" content="${esc(img)}">
<link rel="canonical" href="${esc(target)}">
<meta http-equiv="refresh" content="0; url=${esc(target)}">
<script>location.replace(${JSON.stringify(target)});</script>
</head><body style="font-family:system-ui;background:#0e1119;color:#eef1f8;text-align:center;padding:40px">
Opening today's puzzle… <a style="color:#5aa2ff" href="${esc(target)}">tap here if it doesn't</a>.
</body></html>`;
  return new Response(html, {
    headers: { "content-type": "text/html; charset=utf-8", "cache-control": "public, max-age=300" },
  });
}
