"""
Prototipo de Sistema Universidad Web - Lógica de Negocio
"""

from typing import Dict
import json
import os


class Estudiante:
    """Clase que representa un estudiante"""

    def __init__(self, id: str, nombre: str, email: str, facultad: str, semestre: int):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.facultad = facultad
        self.semestre = semestre
        self.asignaturas = {}

    def agregar_asignatura(self, nombre: str, codigo: str, creditos: int, nota: float):
        """Agregar una asignatura al estudiante"""
        self.asignaturas[codigo] = {
            "nombre": nombre,
            "codigo": codigo,
            "creditos": creditos,
            "nota": nota,
        }

    def obtener_promedio(self) -> float:
        """Calcular promedio de calificaciones"""
        if not self.asignaturas:
            return 0.0
        total_notas = sum(a["nota"] for a in self.asignaturas.values())
        return round(total_notas / len(self.asignaturas), 2)

    def to_dict(self) -> Dict:
        """Convertir estudiante a diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "facultad": self.facultad,
            "semestre": self.semestre,
            "promedio": self.obtener_promedio(),
        }


class Ubicacion:
    """Clase que representa una ubicación en el mapa"""

    def __init__(
        self,
        nombre: str,
        facultad: str,
        latitud: float,
        longitud: float,
        descripcion: str = "",
    ):
        self.nombre = nombre
        self.facultad = facultad
        self.latitud = latitud
        self.longitud = longitud
        self.descripcion = descripcion

    def to_dict(self) -> Dict:
        """Convertir ubicación a diccionario"""
        return {
            "nombre": self.nombre,
            "facultad": self.facultad,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "descripcion": self.descripcion,
        }


class SistemaUniversidad:
    """Sistema principal de la universidad"""

    def __init__(self):
        self.estudiantes = {}
        self.usuario_actual = None
        self.ubicaciones = []
        self.eventos = {}

        # Ruta de datos
        self.ruta_datos = os.path.join(os.path.dirname(__file__), "data")
        self.ruta_estudiantes = os.path.join(self.ruta_datos, "estudiantes.json")
        self.ruta_ubicaciones = os.path.join(self.ruta_datos, "ubicaciones.json")
        self.ruta_eventos = os.path.join(self.ruta_datos, "eventos.json")

        # Asegurar que la carpeta data existe
        os.makedirs(self.ruta_datos, exist_ok=True)

        # Cargar datos desde JSON
        self._cargar_datos()

    def _cargar_datos(self):
        """Cargar datos desde archivos JSON"""
        # Cargar estudiantes
        if os.path.exists(self.ruta_estudiantes):
            try:
                with open(self.ruta_estudiantes, "r", encoding="utf-8") as f:
                    datos_estudiantes = json.load(f)
                    for email, datos in datos_estudiantes.items():
                        estudiante = Estudiante(
                            id=datos["id"],
                            nombre=datos["nombre"],
                            email=datos["email"],
                            facultad=datos["facultad"],
                            semestre=datos["semestre"],
                        )
                        if "asignaturas" in datos:
                            for codigo, asig in datos["asignaturas"].items():
                                estudiante.asignaturas[codigo] = asig

                        # Guardar eventos del estudiante
                        eventos = []
                        if "eventos" in datos:
                            eventos = datos["eventos"]

                        self.estudiantes[email] = {
                            "estudiante": estudiante,
                            "contraseña": datos.get("contraseña", "password"),
                            "eventos": eventos,
                        }
            except Exception as e:
                print(f"Error al cargar estudiantes: {e}")
                self._inicializar_datos_defecto()
        else:
            self._inicializar_datos_defecto()

        # Cargar eventos
        if os.path.exists(self.ruta_eventos):
            try:
                with open(self.ruta_eventos, "r", encoding="utf-8") as f:
                    self.eventos = json.load(f)
            except Exception as e:
                print(f"Error al cargar eventos: {e}")

        # Cargar ubicaciones (estas sí son globales)
        if os.path.exists(self.ruta_ubicaciones):
            try:
                with open(self.ruta_ubicaciones, "r", encoding="utf-8") as f:
                    datos_ubicaciones = json.load(f)
                    self.ubicaciones = [
                        Ubicacion(
                            u["nombre"],
                            u["facultad"],
                            u["latitud"],
                            u["longitud"],
                            u.get("descripcion", ""),
                        )
                        for u in datos_ubicaciones
                    ]
            except Exception as e:
                print(f"Error al cargar ubicaciones: {e}")

    def _inicializar_datos_defecto(self):
        """Inicializar datos de prueba por defecto"""
        estudiante = Estudiante(
            id="2024001",
            nombre="Juan Pérez",
            email="juan.perez@universidad.edu",
            facultad="Ingeniería de Sistemas",
            semestre=4,
        )
        estudiante.agregar_asignatura("Programación Avanzada", "IS201", 3, 4.5)
        estudiante.agregar_asignatura("Bases de Datos", "IS202", 3, 4.2)
        estudiante.agregar_asignatura("Redes de Computadores", "IS203", 3, 4.8)
        estudiante.agregar_asignatura("Ingeniería de Software", "IS204", 4, 4.0)

        self.estudiantes[estudiante.email] = {
            "estudiante": estudiante,
            "contraseña": "password",
        }

        # Guardar datos defecto en JSON
        self._guardar_estudiantes()

    def _guardar_estudiantes(self):
        """Guardar estudiantes en JSON"""
        try:
            datos = {}
            for email, usuario in self.estudiantes.items():
                estud = usuario["estudiante"]
                datos[email] = {
                    "id": estud.id,
                    "nombre": estud.nombre,
                    "email": estud.email,
                    "contraseña": usuario["contraseña"],
                    "facultad": estud.facultad,
                    "semestre": estud.semestre,
                    "asignaturas": estud.asignaturas,
                }
            with open(self.ruta_estudiantes, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar estudiantes: {e}")

    def _guardar_ubicaciones(self):
        """Guardar ubicaciones en JSON"""
        try:
            datos = [ubicacion.to_dict() for ubicacion in self.ubicaciones]
            with open(self.ruta_ubicaciones, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar ubicaciones: {e}")

    def login(self, email: str, contraseña: str) -> Dict:
        """Autenticar usuario"""
        if email not in self.estudiantes:
            return {"success": False, "mensaje": "Email no encontrado"}

        usuario = self.estudiantes[email]
        if usuario["contraseña"] != contraseña:
            return {"success": False, "mensaje": "Contraseña incorrecta"}

        self.usuario_actual = usuario["estudiante"]
        return {
            "success": True,
            "mensaje": f"Bienvenido {usuario['estudiante'].nombre}",
            "estudiante": usuario["estudiante"].to_dict(),
        }

    def logout(self) -> Dict:
        """Cerrar sesión"""
        if self.usuario_actual:
            nombre = self.usuario_actual.nombre
            self.usuario_actual = None
            return {"success": True, "mensaje": f"Hasta luego {nombre}"}
        return {"success": False, "mensaje": "No hay sesión activa"}

    def obtener_perfil(self) -> Dict:
        """Obtener perfil del usuario actual"""
        if not self.usuario_actual:
            return {"success": False, "mensaje": "No hay sesión activa"}

        return {
            "success": True,
            "perfil": {
                "id": self.usuario_actual.id,
                "nombre": self.usuario_actual.nombre,
                "email": self.usuario_actual.email,
                "facultad": self.usuario_actual.facultad,
                "semestre": self.usuario_actual.semestre,
                "promedio": self.usuario_actual.obtener_promedio(),
                "asignaturas": list(self.usuario_actual.asignaturas.values()),
            },
        }

    def obtener_calendario(self, email: str = None) -> Dict:
        """Obtener eventos del calendario del estudiante"""
        usuario = None
        if email and email in self.estudiantes:
            usuario = self.estudiantes[email]
        elif self.usuario_actual:
            for e, datos in self.estudiantes.items():
                if datos["estudiante"] == self.usuario_actual:
                    usuario = datos
                    break

        if not usuario:
            return {
                "success": False,
                "mensaje": "No hay sesión activa",
                "eventos": [],
            }

        evento_ids = usuario.get("eventos", [])
        # Convertir IDs de eventos a datos reales de eventos
        eventos_datos = []
        for evento_id in evento_ids:
            if evento_id in self.eventos:
                evento = self.eventos[evento_id].copy()
                evento["id"] = evento_id
                eventos_datos.append(evento)

        return {
            "success": True,
            "eventos": eventos_datos,
        }

    def obtener_mapa(self) -> Dict:
        """Obtener ubicaciones del mapa"""
        if not self.usuario_actual:
            return {"success": False, "mensaje": "No hay sesión activa"}

        return {
            "success": True,
            "ubicaciones": [ubicacion.to_dict() for ubicacion in self.ubicaciones],
        }

    def obtener_inicio(self, email: str = None) -> Dict:
        """Obtener información de inicio"""
        usuario = None
        if email and email in self.estudiantes:
            usuario = self.estudiantes[email]["estudiante"]
        elif self.usuario_actual:
            usuario = self.usuario_actual

        if not usuario:
            return {
                "success": False,
                "mensaje": "No hay sesión activa",
                "bienvenida": "Error",
            }

        return {
            "success": True,
            "bienvenida": f"¡Bienvenido {usuario.nombre}!",
            "mensaje": "Selecciona una opción del menú",
            "estudiante": usuario.nombre,
        }


def main():
    """Función principal para pruebas en consola (sin servidor web)"""
    print("=" * 50)
    print("PROTOTIPO SISTEMA UNIVERSIDAD WEB")
    print("=" * 50)

    sistema = SistemaUniversidad()

    # Prueba de Login
    print("\n1. PROBANDO LOGIN")
    resultado = sistema.login("juan.perez@universidad.edu", "password")
    print(f"   Resultado: {resultado['mensaje']}")

    # Prueba de Inicio
    print("\n2. PROBANDO INICIO")
    resultado = sistema.obtener_inicio(email="juan.perez@universidad.edu")
    print(f"   {resultado['bienvenida']}")
    print(f"   {resultado['mensaje']}")

    # Prueba de Perfil
    print("\n3. PROBANDO PERFIL")
    resultado = sistema.obtener_perfil()
    if resultado["success"]:
        perfil = resultado["perfil"]
        print(f"   Nombre: {perfil['nombre']}")
        print(f"   ID: {perfil['id']}")
        print(f"   Email: {perfil['email']}")
        print(f"   Facultad: {perfil['facultad']}")
        print(f"   Promedio: {perfil['promedio']}")

    # Prueba de Calendario
    print("\n4. PROBANDO CALENDARIO")
    resultado = sistema.obtener_calendario(email="juan.perez@universidad.edu")
    if resultado["success"]:
        print(f"   Eventos próximos: {len(resultado['eventos'])} eventos")

    # Prueba de Mapa
    print("\n5. PROBANDO MAPA")
    resultado = sistema.obtener_mapa()
    if resultado["success"]:
        print(
            f"   Ubicaciones disponibles: {len(resultado['ubicaciones'])} ubicaciones"
        )

    print("\n" + "=" * 50)
    print("FIN DE PRUEBAS")
    print("=" * 50)


if __name__ == "__main__":
    print("Iniciando Sistema Universidad (modo consola)...")
    main()
