#!/usr/bin/env python
"""
Script para ejecutar el servidor Flask - USAR ESTE ARCHIVO
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(__file__))

from app import app

if __name__ == "__main__":
    print("=" * 50)
    print("SERVIDOR FLASK INICIADO")
    print("=" * 50)
    print("🌐 Abre tu navegador en: http://localhost:9876")
    print("📧 Email: juan.perez@universidad.edu")
    print("🔐 Contraseña: password")
    print("=" * 50)
    print("Presiona CTRL+C para detener el servidor")
    print("=" * 50)
    app.run(debug=True, port=9876, host="127.0.0.1")
