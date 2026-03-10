import json

def cargar_localidad();
    with open("tunjuelito.geojson", "r", encoding="utf-8") as f:
        return json.load(f)
    
def obtener_sitp():
    return{
         "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "nombre": "Paradero SITP Venecia",
                    "ruta": "H605"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [-74.1415, 4.5798]
                }
            },
            {
                "type": "Feature",
                "properties": {
                    "nombre": "Paradero SITP Tunal",
                    "ruta": "B903"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [-74.1388, 4.5739]
                }
            },
            {
                "type": "Feature",
                "properties": {
                    "nombre": "Paradero SITP Meissen",
                    "ruta": "C123"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [-74.1480, 4.5675]
                }
            }
        ]
    }
def obtener_info();
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