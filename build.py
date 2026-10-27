"""Genera index.html (archivo único, funciona sin internet) a partir de src/template.html y libs/."""
import re, base64, pathlib
root = pathlib.Path(__file__).parent
read = lambda p: (root / p).read_text(encoding='utf-8')
t = read('src/template.html')
cj = re.sub(r'^export ', '', read('libs/chess.js'), flags=re.M)   # chess.js 0.13 es ESM; lo usamos como script clásico
sf = read('libs/stockfish.asm.js')                                 # respaldo: Stockfish 10 (asm.js)
sfjs = read('libs/stockfish-19-lite-single.js')                    # motor principal: Stockfish 19 (WASM)
sfw = base64.b64encode((root / 'libs/stockfish-19-lite-single.wasm').read_bytes()).decode()
for x in (cj, sf, sfjs):
    assert '</script' not in x
out = t.replace('__CHESSJS__', cj).replace('__SF__', sf).replace('__SFJS__', sfjs).replace('__SFWASM__', sfw)
(root / 'index.html').write_text(out, encoding='utf-8')
print('index.html generado')
