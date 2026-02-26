"""
Prototipo Web con Flask - Sistema Universidad
"""

## Martin Estrada y Juan Andrés Correa
from flask import Flask, request, session, redirect, url_for
from src.main import SistemaUniversidad

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.secret_key = "clave_secreta_prototipo"

# Iniciailizar sistema
sistema = SistemaUniversidad()


@app.route("/")
def index():
    """Página principal - redirigir a login"""
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Página de login"""
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")

        resultado = sistema.login(email, contraseña)

        if resultado["success"]:
            session["usuario"] = email
            return redirect(url_for("inicio"))
        else:
            return (
                f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error - Universidad</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {{ background: linear-gradient(135deg, #5BC0DE 0%, #4FA3C0 100%); min-height: 100vh; display: flex; align-items: center; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-5">
                            <div class="alert alert-danger text-center" role="alert">
                                <h4 class="alert-heading">❌ Error de Autenticación</h4>
                                <p>{resultado["mensaje"]}</p>
                                <a href="/login" class="btn btn-primary mt-3">Volver al Login</a>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """,
                401,
            )

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login - Sistema Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                background: linear-gradient(135deg, #5BC0DE 0%, #4FA3C0 100%); 
                min-height: 100vh; 
                display: flex; 
                align-items: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                overflow-x: hidden;
            }
            .login-container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                padding: 50px;
                max-width: 450px;
                width: 100%;
            }
            .login-header {
                text-align: center;
                margin-bottom: 40px;
            }
            .login-header h1 {
                font-size: 2.5rem;
                color: #5BC0DE;
                margin-bottom: 10px;
                font-weight: bold;
            }
            .login-header p {
                color: #666;
                font-size: 1rem;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .form-control {
                padding: 12px 15px;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                font-size: 1rem;
                transition: all 0.3s ease;
            }
            .form-control:focus {
                border-color: #667eea;
                box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
                outline: none;
            }
            .form-control::placeholder {
                color: #999;
            }
            .btn-login {
                width: 100%;
                padding: 12px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 1.1rem;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .btn-login:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
                color: white;
            }
            .credentials-info {
                background: #f8f9fa;
                border-left: 4px solid #667eea;
                padding: 15px;
                border-radius: 8px;
                margin-top: 30px;
            }
            .credentials-info h6 {
                color: #667eea;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .credentials-info p {
                color: #666;
                font-size: 0.95rem;
                margin: 5px 0;
            }
            .form-label {
                color: #333;
                font-weight: 600;
                margin-bottom: 8px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center align-items-center" style="min-height: 100vh;">
                <div class="col-md-5">
                    <div class="login-container">
                        <div class="login-header">
                            <h1>🎓</h1>
                            <h1>Universidad</h1>
                            <p>Sistema de Gestión Académica</p>
                        </div>
                        
                        <form method="post" class="login-form">
                            <div class="form-group">
                                <label class="form-label" for="email">📧 Email</label>
                                <input 
                                    type="email" 
                                    class="form-control" 
                                    name="email" 
                                    id="email"
                                    placeholder="ejemplo@universidad.edu" 
                                    required 
                                    value="juan.perez@universidad.edu"
                                >
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label" for="contraseña">🔐 Contraseña</label>
                                <input 
                                    type="password" 
                                    class="form-control" 
                                    name="contraseña" 
                                    id="contraseña"
                                    placeholder="Ingresa tu contraseña" 
                                    required 
                                    value="password"
                                >
                            </div>
                            
                            <button type="submit" class="btn btn-login">
                                <i class="fas fa-sign-in-alt"></i> Ingresar
                            </button>
                        </form>
                        
                        <div class="credentials-info">
                            <h6>ℹ️ Credenciales de Prueba</h6>
                            <p><strong>Email:</strong><br>juan.perez@universidad.edu</p>
                            <p><strong>Contraseña:</strong><br>password</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """


@app.route("/inicio")
def inicio():
    """Página de inicio"""
    if "usuario" not in session:
        return redirect(url_for("login"))

    resultado = sistema.obtener_inicio(email=session["usuario"])

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inicio - Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 40px 20px;
            }}
            .navbar-custom {{
                background: rgba(255, 255, 255, 0.95);
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                border-radius: 10px;
                margin-bottom: 40px;
            }}
            .navbar-brand {{
                font-size: 1.5rem;
                font-weight: bold;
                color: #667eea !important;
            }}
            .welcome-container {{
                text-align: center;
                color: white;
                margin-bottom: 50px;
            }}
            .welcome-container h1 {{
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            .welcome-container p {{
                font-size: 1.2rem;
                opacity: 0.95;
            }}
            .menu-container {{
                max-width: 900px;
                margin: 0 auto;
            }}
            .menu-title {{
                text-align: center;
                color: white;
                font-size: 2rem;
                margin-bottom: 40px;
                font-weight: bold;
            }}
            .card-menu {{
                background: white;
                border: none;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
                overflow: hidden;
                text-decoration: none;
                color: #333;
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 150px;
                cursor: pointer;
                margin-bottom: 25px;
            }}
            .card-menu:hover {{
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                color: #667eea;
            }}
            .card-menu i {{
                font-size: 3rem;
                margin-right: 20px;
                color: #5BC0DE;
            }}
            .card-menu.logout {{
                background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            }}
            .card-menu.logout:hover {{
                color: white;
            }}
            .card-menu.logout i {{
                color: white;
            }}
            .card-menu h3 {{
                font-size: 1.5rem;
                font-weight: bold;
                margin: 0;
            }}
            .footer {{
                text-align: center;
                color: white;
                margin-top: 60px;
                opacity: 0.8;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand navbar-light navbar-custom">
            <div class="container-fluid">
                <span class="navbar-brand">🎓 Sistema Universidad</span>
                <span class="navbar-text ms-auto" style="color: #5BC0DE; font-weight: bold;">
                    <i class="fas fa-user-check"></i> Bienvenido
                </span>
            </div>
        </nav>

        <div class="welcome-container">
            <h1>{resultado["bienvenida"]}</h1>
            <p>{resultado["mensaje"]}</p>
        </div>

        <div class="menu-container">
            <div class="menu-title">Selecciona una opción</div>
            
            <div class="row">
                <div class="col-md-6">
                    <a href="/perfil" class="card-menu d-block">
                        <i class="fas fa-user-circle"></i>
                        <h3>Mi Perfil</h3>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/calendario" class="card-menu d-block">
                        <i class="fas fa-calendar-alt"></i>
                        <h3>Calendario</h3>
                    </a>
                </div>
            </div>
            
            <div class="row">
                <div class="col-md-6">
                    <a href="/mapa" class="card-menu d-block">
                        <i class="fas fa-map"></i>
                        <h3>Mapa Campus</h3>
                    </a>
                </div>
                <div class="col-md-6">
                    <a href="/logout" class="card-menu logout d-block">
                        <i class="fas fa-sign-out-alt"></i>
                        <h3>Cerrar Sesión</h3>
                    </a>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Sistema de Gestión Académica © 2026</p>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """


@app.route("/perfil")
def perfil():
    """Página de perfil"""
    if "usuario" not in session:
        return redirect(url_for("login"))

    resultado = sistema.obtener_perfil()

    if not resultado["success"]:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"

    perfil = resultado["perfil"]
    asignaturas_html = "".join(
        [
            f"""<tr>
            <td><strong>{a["nombre"]}</strong></td>
            <td><span class="badge bg-info">{a["creditos"]}</span></td>
            <td><span class="badge bg-success">{a["nota"]}</span></td>
        </tr>"""
            for a in perfil["asignaturas"]
        ]
    )

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Perfil - Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 40px 20px;
            }}
            .container-main {{
                max-width: 1000px;
                margin: 0 auto;
            }}
            .header {{
                text-align: center;
                color: white;
                margin-bottom: 40px;
            }}
            .header h1 {{
                font-size: 2.5rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            .profile-card {{
                background: white;
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
                margin-bottom: 30px;
            }}
            .profile-info {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .info-box {{
                background: linear-gradient(135deg, #5BC0DE 0%, #4FA3C0 100%);
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
            }}
            .info-box-label {{
                font-size: 0.9rem;
                opacity: 0.9;
                margin-bottom: 5px;
            }}
            .info-box-value {{
                font-size: 1.5rem;
                font-weight: bold;
            }}
            .table {{
                margin-top: 30px;
            }}
            .table thead {{
                background: #667eea;
                color: white;
            }}
            .table tbody tr:hover {{
                background: #f8f9fa;
            }}
            .table-title {{
                font-size: 1.5rem;
                font-weight: bold;
                color: #333;
                margin-top: 30px;
                margin-bottom: 20px;
                border-bottom: 3px solid #5BC0DE;
                padding-bottom: 10px;
            }}
            .btn-back {{
                display: inline-block;
                margin-top: 30px;
                padding: 12px 30px;
                background: #5BC0DE;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: all 0.3s;
                font-weight: bold;
            }}
            .btn-back:hover {{
                background: #4FA3C0;
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(91, 192, 222, 0.3);
                color: white;
            }}
            .badge {{
                padding: 8px 12px;
                font-size: 1rem;
            }}
        </style>
    </head>
    <body>
        <div class="container-main">
            <div class="header">
                <h1>👤 Mi Perfil Académico</h1>
            </div>

            <div class="profile-card">
                <div class="profile-info">
                    <div class="info-box">
                        <div class="info-box-label">Nombre</div>
                        <div class="info-box-value">{perfil["nombre"]}</div>
                    </div>
                    <div class="info-box">
                        <div class="info-box-label">ID Estudiante</div>
                        <div class="info-box-value">{perfil["id"]}</div>
                    </div>
                    <div class="info-box">
                        <div class="info-box-label">Semestre</div>
                        <div class="info-box-value">{perfil["semestre"]}</div>
                    </div>
                    <div class="info-box">
                        <div class="info-box-label">Promedio Académico</div>
                        <div class="info-box-value">{perfil["promedio"]}</div>
                    </div>
                </div>

                <hr style="margin: 30px 0;">

                <div style="text-align: center;">
                    <p><strong>📧 Email:</strong> {perfil["email"]}</p>
                    <p><strong>🏫 Facultad:</strong> {perfil["facultad"]}</p>
                </div>

                <div class="table-title">
                    <i class="fas fa-book"></i> Asignaturas Inscritas
                </div>

                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th><i class="fas fa-book-open"></i> Asignatura</th>
                            <th><i class="fas fa-credit-card"></i> Créditos</th>
                            <th><i class="fas fa-star"></i> Calificación</th>
                        </tr>
                    </thead>
                    <tbody>
                        {asignaturas_html}
                    </tbody>
                </table>

                <a href="/inicio" class="btn-back">
                    <i class="fas fa-arrow-left"></i> Volver al Inicio
                </a>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """


@app.route("/calendario")
def calendario():
    """Página de calendario"""
    if "usuario" not in session:
        return redirect(url_for("login"))

    resultado = sistema.obtener_calendario(email=session["usuario"])

    if not resultado["success"]:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"

    # Organizar eventos por fecha
    eventos_por_fecha = {}
    for evento in resultado["eventos"]:
        fecha = evento["fecha"]
        if fecha not in eventos_por_fecha:
            eventos_por_fecha[fecha] = []
        eventos_por_fecha[fecha].append(evento)

    # Generar HTML de eventos agrupados por fecha
    eventos_html = ""
    for fecha in sorted(eventos_por_fecha.keys()):
        eventos_html += f'<div class="event-date-group"><h3 class="date-header"><i class="fas fa-calendar-check"></i> {fecha}</h3>'
        for evento in eventos_por_fecha[fecha]:
            tipo_clase = evento["tipo"].lower().replace(" ", "-")
            icon_map = {
                "examen": "fa-pencil-alt",
                "entrega": "fa-file-upload",
                "reunion": "fa-users",
                "evento": "fa-star",
                "otra": "fa-circle",
            }
            icon = next(
                (v for k, v in icon_map.items() if k in tipo_clase), "fa-circle"
            )
            eventos_html += f"""<div class="event-card event-{tipo_clase}">
                <div class="event-icon"><i class="fas {icon}"></i></div>
                <div class="event-content">
                    <h4>{evento["nombre"]}</h4>
                    <p class="event-type"><span class="badge">{evento["tipo"]}</span></p>
                    <p class="event-description">{evento["descripcion"]}</p>
                </div>
            </div>"""
        eventos_html += "</div>"

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calendario - Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 40px 20px;
            }}
            .container-main {{
                max-width: 900px;
                margin: 0 auto;
            }}
            .header {{
                text-align: center;
                color: white;
                margin-bottom: 40px;
            }}
            .header h1 {{
                font-size: 2.5rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
                margin-bottom: 10px;
            }}
            .header p {{
                font-size: 1.1rem;
                opacity: 0.95;
            }}
            .calendar-card {{
                background: white;
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
            }}
            .event-date-group {{
                margin-bottom: 35px;
            }}
            .date-header {{
                color: #28a745;
                font-size: 1.3rem;
                font-weight: bold;
                padding-bottom: 15px;
                border-bottom: 3px solid #28a745;
                margin-bottom: 20px;
            }}
            .date-header i {{
                margin-right: 10px;
            }}
            .event-card {{
                display: flex;
                gap: 15px;
                padding: 15px;
                margin-bottom: 15px;
                border-radius: 10px;
                background: #f8f9fa;
                border-left: 5px solid #ccc;
                transition: all 0.3s ease;
            }}
            .event-card:hover {{
                transform: translateX(5px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }}
            .event-card.event-examen {{
                border-left-color: #e74c3c;
                background: rgba(231, 76, 60, 0.05);
            }}
            .event-card.event-entrega {{
                border-left-color: #3498db;
                background: rgba(52, 152, 219, 0.05);
            }}
            .event-card.event-reunion {{
                border-left-color: #f39c12;
                background: rgba(243, 156, 18, 0.05);
            }}
            .event-card.event-evento {{
                border-left-color: #9b59b6;
                background: rgba(155, 89, 182, 0.05);
            }}
            .event-icon {{
                font-size: 2rem;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 50px;
                min-width: 50px;
            }}
            .event-card.event-examen .event-icon {{
                color: #e74c3c;
            }}
            .event-card.event-entrega .event-icon {{
                color: #3498db;
            }}
            .event-card.event-reunion .event-icon {{
                color: #f39c12;
            }}
            .event-card.event-evento .event-icon {{
                color: #9b59b6;
            }}
            .event-content {{
                flex: 1;
            }}
            .event-content h4 {{
                color: #333;
                font-weight: bold;
                margin-bottom: 8px;
                font-size: 1.1rem;
            }}
            .event-type {{
                margin: 8px 0;
            }}
            .event-type .badge {{
                padding: 5px 10px;
                font-size: 0.85rem;
            }}
            .event-description {{
                color: #666;
                font-size: 0.95rem;
                margin: 8px 0 0 0;
            }}
            .btn-back {{
                display: inline-block;
                margin-top: 40px;
                padding: 12px 30px;
                background: #28a745;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: all 0.3s;
                font-weight: bold;
            }}
            .btn-back:hover {{
                background: #20c997;
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(40, 167, 69, 0.3);
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="container-main">
            <div class="header">
                <h1><i class="fas fa-calendar-alt"></i> Calendario Académico</h1>
                <p>Próximos eventos y fechas importantes</p>
            </div>

            <div class="calendar-card">
                {eventos_html}
                
                <a href="/inicio" class="btn-back">
                    <i class="fas fa-arrow-left"></i> Volver al Inicio
                </a>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """


@app.route("/mapa")
def mapa():
    """Página de mapa"""
    if "usuario" not in session:
        return redirect(url_for("login"))

    resultado = sistema.obtener_mapa()

    if not resultado["success"]:
        return f"<h1>Error</h1><p>{resultado['mensaje']}</p>"

    ubicaciones_html = "".join(
        [
            f"""<tr>
            <td><strong>{u["nombre"]}</strong></td>
            <td><span class="badge bg-danger">{u["facultad"]}</span></td>
            <td>{u["descripcion"]}</td>
            <td><small class="text-muted">{u["latitud"]}, {u["longitud"]}</small></td>
        </tr>"""
            for u in resultado["ubicaciones"]
        ]
    )

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mapa - Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 40px 20px;
            }}
            .container-main {{
                max-width: 1200px;
                margin: 0 auto;
            }}
            .header {{
                text-align: center;
                color: white;
                margin-bottom: 40px;
            }}
            .header h1 {{
                font-size: 2.5rem;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }}
            .map-card {{
                background: white;
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
                margin-bottom: 40px;
            }}
            .map-image {{
                width: 100%;
                max-width: 1000px;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                margin-bottom: 40px;
            }}
            .table {{
                margin-top: 30px;
            }}
            .table thead {{
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
                color: white;
            }}
            .table tbody tr {{
                transition: all 0.3s;
            }}
            .table tbody tr:hover {{
                background: #fff3f4;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .badge {{
                padding: 8px 12px;
                font-size: 0.95rem;
            }}
            .btn-back {{
                display: inline-block;
                margin-top: 30px;
                padding: 12px 30px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: all 0.3s;
                font-weight: bold;
            }}
            .btn-back:hover {{
                background: #ee5a6f;
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="container-main">
            <div class="header">
                <h1><i class="fas fa-map-location-dot"></i> Mapa del Campus</h1>
                <p style="margin-top: 10px;">Ubicaciones y edificios de la universidad Javeriana</p>
            </div>

            <div class="map-card">
                <img src="/static/Mapa-Parqueaderos-campus-general-2024-2.jpg.webp" alt="Mapa del Campus" class="map-image">
                
                <h2 style="margin-top: 40px; color: #ff6b6b; margin-bottom: 20px;">
                    <i class="fas fa-building"></i> Ubicaciones del Campus
                </h2>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th><i class="fas fa-building"></i> Ubicación</th>
                            <th><i class="fas fa-school"></i> Facultad</th>
                            <th><i class="fas fa-info-circle"></i> Descripción</th>
                            <th><i class="fas fa-location-dot"></i> Coordenadas</th>
                        </tr>
                    </thead>
                    <tbody>
                        {ubicaciones_html}
                    </tbody>
                </table>

                <a href="/inicio" class="btn-back">
                    <i class="fas fa-arrow-left"></i> Volver al Inicio
                </a>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """


@app.route("/logout")
def logout():
    """Cerrar sesión"""
    resultado = sistema.logout()
    session.pop("usuario", None)

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sesión Cerrada - Universidad</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ 
                background: linear-gradient(135deg, #5BC0DE 0%, #4FA3C0 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .logout-container {{
                background: white;
                border-radius: 15px;
                padding: 50px;
                text-align: center;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                max-width: 500px;
                width: 100%;
            }}
            .logout-icon {{
                font-size: 4rem;
                color: #28a745;
                margin-bottom: 20px;
            }}
            .logout-container h1 {{
                color: #333;
                font-size: 2rem;
                margin-bottom: 15px;
                font-weight: bold;
            }}
            .logout-container p {{
                color: #666;
                font-size: 1.1rem;
                margin-bottom: 30px;
            }}
            .btn-login {{
                display: inline-block;
                padding: 12px 40px;
                background: linear-gradient(135deg, #5BC0DE 0%, #4FA3C0 100%);
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: all 0.3s;
                font-size: 1rem;
            }}
            .btn-login:hover {{
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(91, 192, 222, 0.3);
                color: white;
            }}
            .farewell-message {{
                color: #999;
                margin-top: 30px;
                font-size: 0.95rem;
            }}
        </style>
    </head>
    <body>
        <div class="logout-container">
            <div class="logout-icon">
                <i class="fas fa-check-circle"></i>
            </div>
            <h1>✓ {resultado["mensaje"]}</h1>
            <p>Tu sesión ha sido cerrada correctamente</p>
            <a href="/login" class="btn-login">
                <i class="fas fa-sign-in-alt"></i> Volver al Login
            </a>
            <div class="farewell-message">
                <p>Gracias por usar el Sistema de Gestión Académica</p>
                <p>© 2026 Universidad - Todos los derechos reservados</p>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
