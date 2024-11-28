import json
from datetime import datetime

def guardar_puntaje(nombre, puntaje):
    """
    Guarda el puntaje del jugador en un archivo JSON con el nombre, puntaje y fecha.

    Args:
        nombre (str): Nombre del jugador.
        puntaje (int): Puntuación final del jugador.
    """
    archivo_historial = "historial_puntajes.json"
    nuevo_puntaje = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(archivo_historial, "r", encoding="utf8") as file:
            historial = json.load(file)
    except FileNotFoundError:
        historial = []

    historial.append(nuevo_puntaje)

    with open(archivo_historial, "w", encoding="utf8") as file:
        json.dump(historial, file, ensure_ascii=False, indent=4)