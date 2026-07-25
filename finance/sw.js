// Pocket Ledger Service Worker

const CACHE = 'pocket-ledger-v1';
const APP_SHELL = [
  './',
  './index.html',
  './css/app.css',
  './js/db.js',
  './js/engine.js',
  './js/utils.js',
  './js/app.js',
  './manifest.json',
  './icons/icon-192.svg',
  './icons/icon-512.svg',
];

const CDN = [
  'https://unpkg.com/dexie@3.2.4/dist/dexie.js',
  'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE).then(cache => {
      // Cache app shell (must succeed)
      return cache.addAll(APP_SHELL)
        .then(() => cache.addAll(CDN).catch(() => {})); // CDN best-effort
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Only cache GET requests
  if (event.request.method !== 'GET') return;

  // Network-first for navigation (HTML)
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => caches.match('./index.html'))
    );
    return;
  }

  // Cache-first for app shell and CDN resources
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (response.ok) {
          const clone = response.clone();
          caches.open(CACHE).then(cache => cache.put(event.request, clone));
        }
        return response;
      }).catch(() => cached);
    })
  );
});
