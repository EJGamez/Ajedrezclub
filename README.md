# ChessGame — Entrenador de ajedrez

App web para estudiar y practicar: lecciones guiadas con chat de entrenador (Apertura Catalana), problemas tácticos, partidas contra Stockfish por niveles y creador de lecciones propias.

## Usar
Abre `index.html` en Chrome/Edge (funciona sin internet). Progreso y lecciones propias se guardan en el navegador (exporta/importa JSON desde «Crear lección»).

## Partidas (PGN)
Pestaña «Partidas»: importa archivos `.pgn` (o pega el texto), analiza cada jugada con Stockfish, ve la precisión, la gráfica de ventaja y los momentos críticos, y guarda tus errores como problemas en «Táctica › Mis errores». Hay partidas de prueba en `ejemplos/`. Las partidas contra Stockfish también se pueden exportar a PGN y revisar.

## Repertorio (PGN de estudio)
En «Lecciones › Importar PGN…» carga un PGN de estudio: cada `ChapterName` es un capítulo, se conservan los comentarios, las flechas `[%cal]`/`[%csl]` y las **variantes** `( … )` (en Estudio puedes seguirlas; en Práctica se aceptan como jugadas válidas). Los PGN sin `ChapterName` se convierten en una lección de partidas modelo.

- **Examen** (pestaña Examen): líneas al azar de tu repertorio, jugadas de memoria; salen más las que más fallas y el rival se desvía por tus variantes.
- **Salidas del libro:** al jugar contra Stockfish o abrir una partida importada, la app te dice en qué jugada te saliste de tu repertorio (o el rival). En Progreso › Repertorio ves las salidas más frecuentes, las evaluaciones al salir y puedes guardar los huecos como capítulos de estudio.

## Estructuras de peones
Pestaña «Peones»: 8 estructuras (Carlsbad, peón dama aislado, Stonewall, Maroczy, cadena de la Francesa, India de Rey cerrada, Benoni y Catalana abierta), cada una con su explicación, planes de ambos bandos, errores típicos y 2 posiciones. «Adivina el plan» plantea una pregunta de opción múltiple por posición, explica cada respuesta y guarda tu porcentaje por estructura (se ve en Progreso). Desde cualquier posición puedes pulsar «Jugar desde aquí» para practicarla contra Stockfish.

## Táctica: colecciones de ejercicios
En «Táctica» elige colección: **Básicos y mis errores**, **Mate en 1** (30), **Mate en 2** (40), **Mate en 3** (24) y **Mejorar la posición** (33). Los mates cubren patrones (pasillo, ahogado, jaque doble, escalera, sacrificios de dama/torre/alfil/caballo y mates con cada pieza); la app acepta cualquier mate válido, no solo el de la solución. Los ejercicios de plan (torre a columna abierta, caballo a un puesto fuerte, rupturas, desarrollo…) explican la idea y muestran la evaluación del motor. Todos se generaron y verificaron con Stockfish; tu porcentaje por patrón aparece en Progreso.

## Hoy (plan diario y perfil de debilidades)
La pestaña **Hoy** es la pantalla inicial. Genera cada día un plan según lo que más necesitas (repaso espaciado, examen de repertorio, táctica del tema más débil, estructura de peones, partidas, lecciones), con sesiones de 15/30/45 min, racha de días y minutos de la semana. Debajo muestra tu perfil de debilidades (temas tácticos, estructuras, fase de la partida donde más pierdes y jugadas olvidadas). Todo se calcula con tu actividad guardada en este navegador.

## Sonido
Botón del altavoz en la cabecera: sonidos sintetizados (sin archivos) para jugada, captura, enroque, coronación, jaque, mate, aciertos, errores y fin de partida; volumen ajustable. Opcionalmente, voz en español (leer al entrenador y/o anunciar cada jugada) con el sintetizador del navegador. Todo se guarda en el navegador.

## Desarrollar
Edita `src/template.html` (lecciones en `LESSONS`, problemas en `PUZZLES`, niveles en `LEVELS`) y regenera:

    python3 build.py

## Licencias
Stockfish.js 19 (WASM, lite, GPLv3) como motor principal, Stockfish.js 10 (asm.js) como respaldo y chess.js (BSD), todo en `libs/`. Por incluir Stockfish, el proyecto se distribuye bajo GPLv3.
