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

Cada estructura también existe como **lección** (Lecciones → «Estructura: …»; botón «Ver lección» en Peones): una línea hasta la posición típica, con flechas, casillas clave, planes de cada bando, errores típicos y el razonamiento de cada opción del quiz. No entran en el repertorio ni en el examen.

## Táctica: colecciones de ejercicios
En «Táctica» elige colección: **Básicos y mis errores**, **Mate en 1** (30), **Mate en 2** (40), **Mate en 3** (24) y **Mejorar la posición** (33). Los mates cubren patrones (pasillo, ahogado, jaque doble, escalera, sacrificios de dama/torre/alfil/caballo y mates con cada pieza); la app acepta cualquier mate válido, no solo el de la solución. Los ejercicios de plan (torre a columna abierta, caballo a un puesto fuerte, rupturas, desarrollo…) explican la idea y muestran la evaluación del motor. Todos se generaron y verificaron con Stockfish; tu porcentaje por patrón aparece en Progreso.

## Finales de peones
Tres lecciones (Lecciones → «Finales de peones: básico / intermedio / avanzado») con 12 posiciones: regla del cuadrado, rey en 6ª, casillas clave, oposición, peón de torre, defensa, flanqueo, ruptura 3 contra 3, peón pasado alejado, Réti y zugzwang. Las posiciones y las jugadas clave se verificaron con Stockfish 16; si juegas otra jugada que también gana, se acepta como variante. Los datos están en `ENDS` dentro de `src/template.html`.

## Repertorios incluidos
La app trae de serie la **Defensa Caro-Kann (con negras)**: 11 capítulos de estudio y 8 partidas modelo (Lecciones). Sale de `ejemplos/Defensa_Caro-Kann_Repertorio.pgn`, embebido en `BUILTIN_PGN` dentro de `src/template.html`; para añadir otro basta con agregar un elemento a esa lista. Entra también en Repaso y Examen.

## Respaldo y sincronización
Pestaña **Progreso → Respaldo y sincronización** (y aviso en «Hoy» si llevas más de 14 días sin respaldar):
- **Descargar / importar respaldo:** un `.json` versionado (`format: 1`) con todo tu progreso. Al importar puedes **combinar** (conserva lo mejor de ambos lados: tarjetas más recientes, más aciertos, unión de lecciones, partidas y días) o **reemplazar**.
- **Carpeta sincronizada (Chrome/Edge):** eliges una carpeta (p. ej. dentro de Dropbox u OneDrive); el progreso se guarda ahí solo y al abrir la app en otra PC se combina automáticamente. El navegador pide reactivar el permiso en cada sesión nueva.
- Todo el acceso a datos pasa por el objeto `store` (localStorage), así que más adelante se puede añadir una nube opcional sin tocar el resto.

## Entrenador y alumnos (por archivos)
Funciona sin servidor, intercambiando archivos `.json`:
1. **Entrenador:** en Progreso → «Entrenador y alumnos» activa el *modo entrenador* (aparece la pestaña **Entrenador**). Ahí creas un curso: tareas (completar una lección, X problemas de táctica, preguntas de peones, líneas de examen, tarjetas de repaso, partidas…), fecha límite y nota, e incluyes tus lecciones propias. «Exportar curso» genera el archivo.
2. **Alumno:** en Progreso → «Importar curso o resultados…». Las tareas aparecen en **Hoy** con botón «Ir» y progreso automático. «Enviar resultados» descarga un archivo con su actividad de los últimos 30 días, racha, puntos débiles y avance de tareas.
3. **Entrenador:** importa los resultados (uno o varios archivos) en la pestaña Entrenador: tabla de alumnos (última actividad, minutos, racha, tareas) y detalle con puntos débiles y su evolución entre entregas.
Las lecciones incluidas de la app (estructuras, finales, Caro-Kann, Catalana…) se asignan por nombre; las propias del entrenador viajan dentro del archivo del curso.

## Calcular sin mover piezas
En **Táctica** marca «Calcular sin mover piezas»: el tablero se bloquea y escribes la línea completa (tus jugadas y las respuestas del rival) hasta el mate; la app la comprueba. Notación española (R D T A C) o inglesa a elegir. Resultados: línea correcta, primera jugada correcta pero incompleta, o incorrecta; «Ver solución» la reproduce en el tablero. Sirve con las colecciones de Mate en 1/2/3, básicos y posicionales (en estos últimos se escribe la mejor jugada). Entra en las estadísticas, en el plan de «Hoy» (sesiones de 30/45 min) y se puede asignar como tarea a un alumno.

## Hoy (plan diario y perfil de debilidades)
La pestaña **Hoy** es la pantalla inicial. Genera cada día un plan según lo que más necesitas (repaso espaciado, examen de repertorio, táctica del tema más débil, estructura de peones, partidas, lecciones), con sesiones de 15/30/45 min, racha de días y minutos de la semana. Debajo muestra tu perfil de debilidades (temas tácticos, estructuras, fase de la partida donde más pierdes y jugadas olvidadas). Todo se calcula con tu actividad guardada en este navegador.

## Sonido
Botón del altavoz en la cabecera: sonidos sintetizados (sin archivos) para jugada, captura, enroque, coronación, jaque, mate, aciertos, errores y fin de partida; volumen ajustable. Opcionalmente, voz en español (leer al entrenador y/o anunciar cada jugada) con el sintetizador del navegador. Todo se guarda en el navegador.

## Desarrollar
Edita `src/template.html` (lecciones en `LESSONS`, problemas en `PUZZLES`, niveles en `LEVELS`) y regenera:

    python3 build.py

## Licencias
Stockfish.js 19 (WASM, lite, GPLv3) como motor principal, Stockfish.js 10 (asm.js) como respaldo y chess.js (BSD), todo en `libs/`. Por incluir Stockfish, el proyecto se distribuye bajo GPLv3.

## Crear lecciones e importar PGN
- **Lecciones → Importar PGN**: acepta PGN de estudios (Lichess/ChessBase) con comentarios, `[Orientation]`, flechas `[%cal]` y varias partidas. El color (blancas/negras) se detecta solo; también puedes elegirlo, y elegir si cada partida es un capítulo o una partida modelo. Si el PGN trae notación en español (R, D, T, A, C) se convierte automáticamente. Si algo falla, el mensaje indica qué partida y qué jugada.
- **Crear**: editor de lecciones con varios capítulos (añadir, borrar, ordenar), posición inicial por FEN, comentario por jugada, pegar jugadas/PGN, editar tus lecciones o copiar una incluida, duplicar/borrar, y guardar o guardar y practicar.
- **Importar/exportar** desde Crear: PGN o JSON (una lección, una lista o `{lessons}`); exportar la lección actual (JSON o PGN) o todas las tuyas.
