import json
import pygame
import sys
from modulos.guardar_datos import guardar_config
from modulos.contorno import dibujar_texto_con_contorno
from modulos.cargar_datos import cargar_config
def bubble_sort(historial):
    """
    Ordena una lista de diccionarios que contienen puntajes usando el algoritmo Bubble Sort.
    
    Args:
        historial (list): Lista de diccionarios con puntajes.
        
    Returns:
        list: Lista ordenada de puntajes de mayor a menor.
    """
    n = len(historial)
    for i in range(n):
        for j in range(0, n-i-1):
            if historial[j]["puntaje"] < historial[j+1]["puntaje"]:
                historial[j], historial[j+1] = historial[j+1], historial[j]
    return historial

def mostrar_tabla_puntuaciones(font, small_font, screen, cambiar_fondo, OPCIONES_IMAGE, reproducir_sonido_func, sonidos, WIDTH, HEIGHT, BLACK, GOLD, SILVER, BROWN):
    """
    Muestra la tabla de puntuaciones ordenada.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        small_font (pygame.font.Font): Fuente secundaria.
        screen (pygame.Surface): Superficie de la pantalla.
        cambiar_fondo (function): Función para cambiar el fondo.
        OPCIONES_IMAGE (pygame.Surface): Imagen para botones.
        reproducir_sonido (function): Función para reproducir sonidos.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        BLACK (tuple): Color negro.
        GOLD (tuple): Color oro.
        SILVER (tuple): Color plata.
        BROWN (tuple): Color marrón.
    """
    estado_config = cargar_config()

    if estado_config is None:
        print("Error: No se pudo cargar la configuración.")
        pygame.quit()
        sys.exit()

    activo = True

    try:
        with open("historial_puntajes.json", "r", encoding="utf8") as file:
            historial = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        historial = []

    historial = bubble_sort(historial)

    while activo:
        cambiar_fondo("modulos/assets/fondo_tabla_puntuaciones.png")
        
        dibujar_texto_con_contorno("Tabla de Puntuaciones", font, (255, 255, 255), BLACK, WIDTH // 2 - font.size("Tabla de Puntuaciones")[0] // 2, 50, screen)

        contador = 0
        for registro in historial[:10]:
            if contador == 0:
                color = GOLD
            elif contador == 1:
                color = SILVER
            elif contador == 2:
                color = BROWN
            else:
                color = (255, 255, 255)

            dibujar_texto_con_contorno(
                f"{contador + 1}. {registro['nombre']} - {registro['puntaje']} pts - {registro['fecha']}",
                small_font,
                color,
                BLACK,
                100,
                150 + contador * 50,
                screen
            )
            contador += 1

        volver_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(OPCIONES_IMAGE, volver_button_rect.topleft)
        dibujar_texto_con_contorno("Volver al menú", small_font, (255, 255, 255), BLACK, volver_button_rect.centerx - small_font.size("Volver al menú")[0] // 2, volver_button_rect.centery - small_font.get_height() // 2, screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_config(None, None)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if volver_button_rect.collidepoint(mouse_pos):
                        volumen_sonido = estado_config["sounds_volume"]
                        
                        for nombre, sonido in sonidos.items():
                            sonido.set_volume(volumen_sonido)
                        
                        reproducir_sonido_func("tocar_opcion", sonidos, estado_config, None)
                        activo = False
