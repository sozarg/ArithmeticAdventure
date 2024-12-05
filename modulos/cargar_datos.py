import pygame
import sys
import json
import csv

def cargar_problemas():
    """
    Carga los problemas matemáticos desde un archivo CSV.
    
    Returns:
        dict: Diccionario con niveles y sus respectivas ecuaciones y resultados.
    """
    niveles = {str(i): [[], []] for i in range(1, 6)}
    try:
        with open("problemas.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file)
            next(reader)
            for fila in reader:
                dificultad, ecuacion, resultado = fila
                niveles[dificultad][0].append(ecuacion.strip())
                niveles[dificultad][1].append(int(resultado.strip()))
    except FileNotFoundError:
        print("Error: El archivo 'problemas.csv' no se encontró.")
        pygame.quit()
        sys.exit()
    return niveles

def cargar_comodines(rutas_comodines, GRAY):
    """
    Carga las imágenes de los comodines y crea una lista de comodines con sus propiedades.
    
    Args:
        rutas_comodines (dict): Rutas de las imágenes de los comodines.
        GRAY (tuple): Color gris para superficies de fallback.
        
    Returns:
        list: Lista de comodines con imágenes y estados.
    """
    comodines = []
    nombres_comodines = ["ganar_vida", "congelar_tiempo", "ganar_ronda"]
    ancho_comodin, alto_comodin = 100, 150
    cantidad_comodines = len(nombres_comodines)

    espacio_disponible = 720 - 2 * 80
    espacio_total_comodines = cantidad_comodines * alto_comodin
    espacio_restante = espacio_disponible - espacio_total_comodines

    espacio_entre = espacio_restante // (cantidad_comodines + 1)

    pos_x = 20
    pos_y = 80 + espacio_entre

    for nombre in nombres_comodines:
        imagen_disponible = cargar_imagen(rutas_comodines[nombre], (ancho_comodin, alto_comodin), GRAY)
        imagen_usado = cargar_imagen(rutas_comodines["usado"], (ancho_comodin, alto_comodin), GRAY)
        rect = imagen_disponible.get_rect(topleft=(pos_x, pos_y))
        comodin = {
            "nombre": nombre,
            "imagen_disponible": imagen_disponible,
            "imagen_usado": imagen_usado,
            "rect": rect,
            "usado": False
        }
        comodines.append(comodin)
        pos_y += alto_comodin + espacio_entre

    return comodines


def cargar_config():
    """
    Carga la configuración del juego desde un archivo JSON.
    Si el archivo no existe o está malformado, no asigna valores por defecto.
    
    Returns:
        dict: Configuración del juego con volúmenes de música y sonidos.
    """
    try:
        with open("config.json", "r", encoding="utf8") as file:
            config = json.load(file)
            music_volume = float(config.get("music_volume", 0.5))
            sounds_volume = float(config.get("sounds_volume", 0.5))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error al cargar la configuración desde config.json: {e}")
        return {"music_volume": 0.5, "sounds_volume": 0.5}
    
    return {"music_volume": music_volume, "sounds_volume": sounds_volume}

def cargar_imagen(ruta, tamaño, GRAY):
    """
    Carga una imagen desde la ruta especificada y la escala al tamaño dado.
    Si falla la carga, retorna una superficie gris del tamaño especificado.
    
    Args:
        ruta (str): Ruta de la imagen.
        tamaño (tuple): Tamaño al que se escalará la imagen.
        GRAY (tuple): Color gris para la superficie de fallback.
        
    Returns:
        pygame.Surface: Imagen cargada y escalada o una superficie gris.
    """
    try:
        imagen = pygame.image.load(ruta).convert_alpha()
        imagen = pygame.transform.scale(imagen, tamaño)
        return imagen
    except pygame.error as e:
        print(f"Error al cargar imagen {ruta}: {e}")
        imagen = pygame.Surface(tamaño)
        imagen.fill(GRAY)
        return imagen