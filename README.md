# Child

App para familias (embarazo, controles, hitos, crecimiento, registro diario y señales de alarma), en un solo HTML sin conexión. Autor: Gonzalo Gabriel Pereira.

- `PROYECTO.md`: decisiones de marca, estado, reglas de trabajo y hoja de ruta. Leer antes de tocar nada.
- `src/index.src.html`: código fuente de la app.
- `src/build.py`: genera `src/index.html` con el logo y los íconos embebidos (`cd src && python3 build.py`).
- `src/mkdoc.py`: genera `proyecto.html` a partir de `PROYECTO.md` (correr desde la raíz: `python3 src/mkdoc.py`).
- `index.html` (raíz): última versión compilada; es la que abre la dirección web.
- `app/`: la misma versión compilada, con su número (`Child_vX.Y.html`).

Una tarea programada diaria avanza un paso y sube cada versión a la rama `main`.
