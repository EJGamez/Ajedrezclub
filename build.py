"""Genera index.html (archivo único, funciona sin internet) a partir de src/template.html y libs/."""
import re, base64, pathlib, hashlib, datetime, json
root = pathlib.Path(__file__).parent
read = lambda p: (root / p).read_text(encoding='utf-8')
t = read('src/template.html')
cj = re.sub(r'^export ', '', read('libs/chess.js'), flags=re.M)   # chess.js 0.13 es ESM; lo usamos como script clásico
sf = read('libs/stockfish.asm.js')                                 # respaldo: Stockfish 10 (asm.js)
sfjs = read('libs/stockfish-19-lite-single.js')                    # motor principal: Stockfish 19 (WASM)
sfw = base64.b64encode((root / 'libs/stockfish-19-lite-single.wasm').read_bytes()).decode()
for x in (cj, sf, sfjs):
    assert '</script' not in x
build = datetime.date.today().isoformat()
out = t.replace('__BUILD__', build).replace('__CHESSJS__', cj).replace('__SF__', sf).replace('__SFJS__', sfjs).replace('__SFWASM__', sfw)
(root / 'index.html').write_text(out, encoding='utf-8')

# --- archivos para publicar como web / app instalable (GitHub Pages) ---
h = hashlib.md5(out.encode()).hexdigest()[:10]
(root / 'sw.js').write_text('''/* Generado por build.py: caché sin conexión. Primero red (siempre la versión nueva), si no hay red, la copia guardada. */
const V='cg-%s';
const ASSETS=['./','./index.html','./manifest.webmanifest','./icons/icon.svg','./icons/icon-192.png','./icons/icon-512.png','./icons/icon-180.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==location.origin)return;
  e.respondWith(fetch(r).then(res=>{if(res.ok){const c=res.clone();caches.open(V).then(x=>x.put(r,c))}return res}).catch(()=>caches.match(r).then(m=>m||caches.match('./index.html'))));
});
''' % h, encoding='utf-8')
(root / 'manifest.webmanifest').write_text(json.dumps({
  'name':'Entrenador de Ajedrez','short_name':'Ajedrez','description':'Entrenador de ajedrez que funciona sin conexión','lang':'es',
  'start_url':'./index.html','scope':'./','display':'standalone','background_color':'#161512','theme_color':'#161512',
  'icons':[{'src':'icons/icon-192.png','sizes':'192x192','type':'image/png','purpose':'any maskable'},{'src':'icons/icon-512.png','sizes':'512x512','type':'image/png','purpose':'any maskable'},{'src':'icons/icon.svg','sizes':'any','type':'image/svg+xml'}]
}, ensure_ascii=False, indent=2), encoding='utf-8')
(root / '.nojekyll').write_text('', encoding='utf-8')
print('index.html generado (build %s, caché %s)' % (build, h))
