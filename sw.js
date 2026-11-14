/* Sin caché a propósito: siempre se ve la última versión publicada. Solo permite instalar la app. */
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',()=>{});
