## Flask Web Prototype - University System

Web prototype for a **University Academic Management System**, built in Python using Flask.  
It allows a student to log in, see a home page, consult their academic profile, review the calendar of events, and view a campus map.

### Technologies used

- **Language**: Python 3 (3.8+ recommended)
- **Web framework**: Flask
- **Frontend**:
  - Bootstrap 5 (via CDN)
  - Font Awesome (icons, via CDN)
- **Data persistence**:
  - JSON files (`estudiantes.json`, `ubicaciones.json`, `eventos.json`)
- **Other**:
  - Session management with `Flask.session`
  - Basic layered structure: business logic vs. web layer

### Project structure

- **`run.py`**: recommended script to start the Flask server (**use this file**).
- **`app.py`**: Flask application (routes and embedded HTML views for login, home, profile, calendar, and map).
- **`src/`**: Python source code.
  - **`src/__init__.py`**: marks the Python package.
  - **`src/main.py`**: business logic:
    - Classes `Estudiante`, `Ubicacion`.
    - Class `SistemaUniversidad` (login, logout, profile, calendar, map, loading/saving JSON data).
    - `main()` function to test the logic in the console (no web server).
- **`data/`** (created automatically if it does not exist): JSON files with sample data.
  - `estudiantes.json`
  - `ubicaciones.json`
  - `eventos.json`
- **`static/`**: static assets.
  - Campus map image (`Mapa-Parqueaderos-campus-general-2024-2.jpg.webp`) used in the map view.

### UML diagrams

This prototype is accompanied by **UML diagrams** that document the system design. The following six diagrams were created:

1. **Use Case Diagram – Student Interaction with the System**  
   Shows the main use cases for the student actor: logging in, viewing the home page, consulting the profile, checking the academic calendar, and viewing the campus map.

2. **Class Diagram – Core Academic Domain**  
   Describes the main classes (`Estudiante`, `Ubicacion`, `SistemaUniversidad`), their attributes, methods, and relationships (e.g., how a `SistemaUniversidad` aggregates students, events, and locations).

3. **Sequence Diagram – Login Flow**  
   Details the interaction between the browser, Flask application (`app.py`), and the business logic (`SistemaUniversidad.login`) when a user submits their email and password and receives either an error message or access to the system.

4. **Sequence Diagram – View Student Profile**  
   Shows the flow from the authenticated student requesting the `/perfil` route, through the Flask controller, to the `SistemaUniversidad.obtener_perfil` method, and back to the rendered HTML with academic information.

5. **Activity Diagram – Academic Calendar Consultation**  
   Represents the steps involved when the student accesses the calendar: verifying the session, loading event IDs, resolving them to event details from JSON, grouping them by date, and finally displaying them in the UI.

6. **Component/Deployment Diagram – Web Prototype Architecture**  
   Illustrates the high-level architecture: browser (client), Flask web server, business logic module (`src/main.py`), and the local JSON data storage, plus how static resources (CSS, JS, images) are served.

The source files of these diagrams (e.g., from draw.io, Lucidchart, PlantUML, etc.) are intended to be stored under a directory such as:

- `docs/diagrams/`

and can be referenced in accompanying documentation or reports.

### How to run the project

1. **Clone or copy the project** to your local machine.
2. **Install dependencies** (at least Flask):

   ```bash
   pip install flask
   ```

3. **Start the Flask server** from the project root:

   ```bash
   python run.py
   ```

4. Open your browser at:

   - `http://localhost:9876`

5. **Test credentials** (also shown in the HTML views):

   - Email: `juan.perez@universidad.edu`
   - Password: `password`

### Testing the business logic (console mode)

If you want to test only the business logic without running the web server, you can execute:

```bash
python -m src.main
```

This runs the `main()` function in `src/main.py`, which performs basic checks of:

- Login
- Home page information
- Student profile
- Events calendar
- Campus locations

