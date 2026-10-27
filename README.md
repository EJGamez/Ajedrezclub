# ChessGame — Entrenador de ajedrez

App web para estudiar y practicar: lecciones guiadas con chat de entrenador (Apertura Catalana), problemas tácticos, partidas contra Stockfish por niveles y creador de lecciones propias.

## Usar
Abre `index.html` en Chrome/Edge (funciona sin internet). Progreso y lecciones propias se guardan en el navegador (exporta/importa JSON desde «Crear lección»).

## Partidas (PGN)
Pestaña «Partidas»: importa archivos `.pgn` (o pega el texto), analiza cada jugada con Stockfish, ve la precisión, la gráfica de ventaja y los momentos críticos, y guarda tus errores como problemas en «Táctica › Mis errores». Hay partidas de prueba en `ejemplos/`. Las partidas contra Stockfish también se pueden exportar a PGN y revisar.

## Desarrollar
Edita `src/template.html` (lecciones en `LESSONS`, problemas en `PUZZLES`, niveles en `LEVELS`) y regenera:

    python3 build.py

## Licencias
Stockfish.js 19 (WASM, lite, GPLv3) como motor principal, Stockfish.js 10 (asm.js) como respaldo y chess.js (BSD), todo en `libs/`. Por incluir Stockfish, el proyecto se distribuye bajo GPLv3.
