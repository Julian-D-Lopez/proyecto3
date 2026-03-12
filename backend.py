# backend.py
import json
from pathlib import Path

def cargar_localidad():
    # asume tunjuelito.geojson en la raíz del proyecto
    path = Path(__file__).parent / "tunjuelito.geojson"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def obtener_sitp():
    import json
    from pathlib import Path
    
    path = Path(__file__).parent / "static" / "paraderos_tunjuelito.geojson"
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def obtener_info():
    return {
        "nombre": "Tunjuelito",
        "descripcion": "Tunjuelito es una localidad de Bogotá ubicada en el sur de la ciudad. Para este proyecto se representa con un polígono GeoJSON y estaciones SITP de ejemplo.",
        "area": "Aproximadamente 9.9 km²",
        "poblacion": "Información de ejemplo para fines académicos",
        "caracteristicas": [
            "Ubicación al sur de Bogotá",
            "Cuenta con corredores viales importantes",
            "Se conecta con rutas del SITP",
            "Ejemplo académico para mapa interactivo"
        ]
    }