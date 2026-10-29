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

## Probar y compartir (versión beta)

**Como página web (GitHub Pages).** En el repositorio: *Settings → Pages → Build and deployment → Deploy from a branch → Branch `main`, carpeta `/ (root)` → Save*. En un minuto queda publicada en `https://TU-USUARIO.github.io/ChessGame/`. Ese enlace es el que se comparte. Desde el móvil o el navegador de escritorio se puede **instalar como aplicación** (Ajustes ⚙ → «Instalar como aplicación», o «Añadir a pantalla de inicio» en iPhone) y después funciona **sin conexión**.

**Como archivo descargable.** Basta con enviar `index.html` (≈4 MB): es la aplicación completa, también el motor Stockfish. Se abre con doble clic en cualquier navegador y no necesita internet.

**Importante:** el progreso se guarda en el navegador y *por dirección*: la versión web, la instalada y el archivo abierto desde el disco tienen datos separados. Para pasar de una a otra se usa el respaldo (Ajustes → Descargar respaldo → Más opciones).

**Qué ve quien la prueba.** Al abrirla por primera vez aparece una bienvenida (explica que los datos quedan en su dispositivo, permite hacer la prueba de nivel o cargar **10 partidas de ejemplo**). El botón **💬** (y Ajustes) abre «Enviar comentarios»: valoración de 1 a 5 de cada apartado, comentarios libres y, opcionalmente, datos técnicos (versión, navegador, errores recientes) y contadores de uso. Se genera un texto que la persona **copia o descarga** y te envía por el medio que prefiera. La aplicación no hace ninguna petición a servidores externos ni envía nada por sí sola.

**Publicar una versión nueva.** Editar `src/template.html`, ejecutar `python3 build.py` (regenera `index.html`, `sw.js` y `manifest.webmanifest`; sube el número de `APP_VERSION` en la plantilla si quieres que aparezca en los comentarios) y hacer commit + push. El servicio sin conexión busca siempre primero la versión nueva.

Archivos de publicación: `index.html`, `sw.js`, `manifest.webmanifest`, `icons/`, `.nojekyll`.

## Licencias
Stockfish.js 19 (WASM, lite, GPLv3) como motor principal, Stockfish.js 10 (asm.js) como respaldo y chess.js (BSD), todo en `libs/`. Por incluir Stockfish, el proyecto se distribuye bajo GPLv3.

## Crear lecciones e importar PGN
- **Lecciones → Importar PGN**: acepta PGN de estudios (Lichess/ChessBase) con comentarios, `[Orientation]`, flechas `[%cal]` y varias partidas. El color (blancas/negras) se detecta solo; también puedes elegirlo, y elegir si cada partida es un capítulo o una partida modelo. Si el PGN trae notación en español (R, D, T, A, C) se convierte automáticamente. Si algo falla, el mensaje indica qué partida y qué jugada.
- **Crear**: editor de lecciones con varios capítulos (añadir, borrar, ordenar), posición inicial por FEN, comentario por jugada, pegar jugadas/PGN, editar tus lecciones o copiar una incluida, duplicar/borrar, y guardar o guardar y practicar.
- **Importar/exportar** desde Crear: PGN o JSON (una lección, una lista o `{lessons}`); exportar la lección actual (JSON o PGN) o todas las tuyas.

## Interfaz
- Botones, campos y paneles con un estilo único; foco visible con teclado; cabecera fija y compacta en pantallas medianas.
- **Crear** se organiza en pestañas (1·Lección, 2·Capítulo, 3·Jugadas, Archivo) con barra fija de «Guardar lección / Guardar y practicar». Nada se desborda del panel; en móvil el panel fluye bajo el tablero.

## Análisis por lotes y diagnóstico (Partidas)
- **Analizar todas**: revisa con Stockfish todas las partidas importadas que aún no lo estén (velocidad Rápida o Normal; se puede detener y se conserva lo ya analizado).
- **Mi diagnóstico**: usa tu nombre de usuario (la app sugiere el más frecuente en tus PGN) para separar tus jugadas y muestra: «qué estudiar primero», rendimiento por color y por fase (apertura/medio juego/final), tipos de error (mates, piezas en prise, capturas o jaques no vistos, posicionales), tus aperturas con precisión y ventaja a la jugada 10, conversión de ventajas (con botón «Convertir» para jugar desde esa posición contra Stockfish) y tus errores más costosos.
- **Guardar todos mis errores como problemas** los añade a Táctica › Básicos y mis errores. El plan de «Hoy» también muestra líneas del diagnóstico.

## A ciegas
Pestaña «A ciegas»: partida contra Stockfish sin ver las piezas. Escribes cada jugada (notación española o inglesa; también e2e4) y el rival se anuncia en texto y, opcionalmente, en voz alta. Opciones: piezas visibles (ninguna / solo peones / solo las mías / todas), ocultar la lista de jugadas, «Ver tablero (3 s)» y «Lista de piezas» (cuentan como vistazos), preguntas «¿qué hay en e5?», entrenamiento del color de las casillas y estadísticas (intentos no válidos, vistazos, aciertos).

## Evolución (Progreso › Evolución)
Gráficas de tu Elo (lo anotas tú, por plataforma), precisión por partida analizada con media móvil, comparación de tus últimas 10 partidas contra las 10 anteriores, minutos de estudio por semana, acierto semanal y acierto por tema de táctica (este último se va llenando con el uso). Cada gráfica tiene «Ver como tabla».

## Objetivos y plan personal (Progreso › Objetivos)
Define una meta de Elo con fecha, minutos de estudio por semana y errores serios por partida. La app calcula el ritmo necesario frente a tu ritmo real, sugiere una sesión diaria y muestra un resumen semanal (semana pasada vs esta). «Hoy» muestra la tarjeta «Tu objetivo» y ajusta el plan (más táctica si tus errores superan la meta).

## Mis errores con repaso espaciado
Los errores de tus partidas analizadas se convierten en ejercicios (Táctica › Mis errores (repaso)) con intervalos de 1, 3, 7, 14, 30 y 60 días. Fallar reinicia la racha; con 4 aciertos seguidos el error se da por dominado. «Hoy» incluye la tarea de repasarlos.

## Cuaderno de partidas (Partidas)
Cada partida tiene su bloque «Notas y etiquetas»: marca **⚑ Para revisar** o **★ Favorita**, tus propias etiquetas, una nota general y **notas por jugada** (avanza a la jugada y guarda el comentario; luego vuelves a ella desde la lista). El botón «Cuaderno» abre la lista con búsqueda de texto (jugadores, apertura, notas, etiquetas) y filtros por marca, resultado, color, etiqueta y «con errores serios». Se añaden etiquetas automáticas (color, resultado, apertura). «Hoy» avisa cuántas partidas tienes marcadas para revisar. Las notas entran en el respaldo y la sincronización.

## Prueba de nivel (Progreso › Nivel)
14 ejercicios (mates en 1, 2 y 3 y posiciones de plan) con una sola oportunidad cada uno, sin pistas ni solución. Da el resultado por área, el tiempo medio y un nivel **orientativo** (no sustituye tu Elo real). Señala tu área más débil con un botón para entrenarla. Se puede repetir (cada mes se sugiere en «Hoy»), prefiriendo ejercicios que no hayas visto. Si sales de Táctica a mitad de la prueba, no se guarda. También se corrigió que los mates se contaran bajo un tema sin nombre en las estadísticas de táctica.

## Retos (pestaña «Retos»)
Tres modos de práctica:

- **Contrarreloj.** Resuelve el máximo de mates y tácticas en 1, 3 o 5 minutos. Empiezan fáciles y se endurecen; tienes 3 vidas, y cada 5 aciertos seguidos suman un punto extra. Guarda tu récord por configuración y cada ejercicio cuenta en tus estadísticas de táctica.
- **Finales teóricos.** 18 posiciones clásicas (peones: rey en sexta, oposición, peón de torre, regla del cuadrado; alfil: alfil equivocado y correcto; torre: Lucena y Philidor; dama: contra peón en séptima, ganadora y de tablas; mates básicos: torre, dama, dos alfiles, alfil y caballo) que juegas contra Stockfish al máximo. Si el objetivo es ganar, hay que coronar o dar mate; si es empatar, hay que resistir, lograr ahogado o que Stockfish acepte tablas. Stockfish evalúa cada jugada: te avisa de imprecisiones y termina el intento si dejas escapar la victoria o las tablas. Hay pista, «Ver la idea», deshacer y reiniciar; solo se considera «dominado» si lo logras sin ayudas. «Hoy» sugiere un final en sesiones de 30 y 45 minutos.
- **Partida con reloj.** Ritmos de 1+0 a 30+0 con incremento, contra Stockfish con el nivel que elijas. Si se acaba tu tiempo, pierdes (o tablas si el rival no puede dar mate). Al terminar, informe de gestión del tiempo: tiempo por fase, jugadas más lentas, errores con poco tiempo o con prisa y consejos. Las partidas cuentan en tus estadísticas.

## Explorador de aperturas (pestaña «Aperturas»)
Construido con tus partidas importadas (necesita tu nombre de usuario tal como aparece en el PGN). Elige si juegas con blancas o negras y mueve las piezas del tablero o pulsa una jugada de la tabla: para cada posición ves qué jugaste tú y qué jugaron tus rivales, cuántas veces, el resultado (barra de ganadas/tablas/perdidas), los puntos y la precisión media (si analizaste las partidas). Se cruza con tu repertorio: 📖 marca lo que está en el libro, ⚠ lo que juegas fuera de él, «hueco» las respuestas del rival que no cubres (con botón «+ Hueco» para guardarlas), y avisa cuando sueles jugar algo distinto de lo que dice tu repertorio. En el inicio aparecen «Donde más puntos pierdes» y «Tus mejores líneas» (líneas con al menos 3 partidas), y cada posición lista las partidas que pasaron por ella, que se abren en Partidas en esa jugada.

## Ajustes (botón ⚙ o tecla «?»)
Tema oscuro, claro o automático; colores del tablero (madera, verde, azul, gris, coral); tamaño del texto; mostrar u ocultar coordenadas, puntos de jugadas legales, resaltado de la última jugada y barra de evaluación; empezar en «Hoy» o donde lo dejaste; pantalla completa; descarga de respaldo, restablecer ajustes y borrar todos los datos (con doble confirmación). Atajos: ← → (jugadas), Inicio/Fin, F (girar), M (sonido), ? (ajustes), Esc (cerrar). La aplicación funciona sin conexión porque es un único archivo; los ajustes son de cada navegador y no se sincronizan entre equipos.
