import pygame
import sys
from modulos.guardar_datos import guardar_config
from modulos.comodines import usar_comodin
from modulos.cargar_datos import cargar_imagen
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

pygame.font.init()

small_font = pygame.font.Font("modulos/assets/Crang.ttf", 30)

def hacer_pregunta(ecuacion, opciones, vidas, puntuacion, nivel, ronda, tiempo_restante, comodines_disponibles, ecuaciones, resultados, tiempo_congelado_flag, comodines_obj, mostrar_hud_func, dibujar_comodines_func, dibujar_opciones_func, cambiar_fondo_func, sonidos, reproducir_sonido_func, BLACK, RED, WIDTH, HEIGHT, screen, estado_config):
    """
    Maneja la lógica de una pregunta dentro del juego, incluyendo el tiempo, la selección de respuestas y el uso de comodines.
        
    Args:
        ecuacion (str): Ecuación actual.
        opciones (list): Lista de opciones de respuesta.
        vidas (int): Número de vidas del jugador.
        puntuacion (int): Puntuación del jugador.
        nivel (int): Nivel actual.
        ronda (int): Ronda actual.
        tiempo_restante (int): Tiempo restante para responder.
        comodines_disponibles (dict): Comodines disponibles.
        ecuaciones (list): Lista de todas las ecuaciones del nivel.
        resultados (list): Lista de resultados correspondientes a las ecuaciones.
        tiempo_congelado_flag (list): Bandera de tiempo congelado.
        comodines_obj (list): Lista de objetos de comodines.
        mostrar_hud_func (function): Función para mostrar el HUD.
        dibujar_comodines_func (function): Función para dibujar comodines.
        dibujar_opciones_func (function): Función para dibujar opciones de respuesta.
        cambiar_fondo_func (function): Función para cambiar el fondo.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        reproducir_sonido_func (function): Función para reproducir sonidos.
        BLACK (tuple): Color negro.
        RED (tuple): Color rojo.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        screen (pygame.Surface): Superficie de la pantalla.
        estado_config (dict): Configuración actual del juego.
        
    Returns:
        tuple: Respuesta seleccionada y actualización de vidas, ronda, puntuación, tiempo restante y bandera de tiempo congelado.
    """
    reloj = pygame.time.Clock()
    ultimo_tick = pygame.time.get_ticks()
    respuesta_seleccionada = False
    selected_response = None

    while True:
        cambiar_fondo_func("modulos/assets/fondo_juego.png")
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - ultimo_tick) // 1000

        if not tiempo_congelado_flag[0]:
            if elapsed_time >= 1:
                tiempo_restante -= 1
                ultimo_tick = current_time

        if tiempo_restante <= 0 and not respuesta_seleccionada:
            vidas -= 1
            reproducir_sonido_func("opcion_incorrecta", sonidos, estado_config, None)
            selected_response = "tiempo_agotado"
            respuesta_seleccionada = True

        mostrar_hud_func(vidas, puntuacion, nivel, ronda, ecuacion, tiempo_restante, tiempo_congelado_flag[0])
        dibujar_comodines_func(comodines_obj, comodines_disponibles, screen, WIDTH, HEIGHT)
        opcion_rects = dibujar_opciones_func(opciones, small_font, WIDTH, BLACK, GRAY, screen)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_config(None, estado_config)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not respuesta_seleccionada:
                if event.button == 1:
                    mouse_pos = event.pos
                    comodin_usado = False
                    for comodin in comodines_obj:
                        if comodin["rect"].collidepoint(mouse_pos) and not comodin["usado"] and comodines_disponibles[comodin["nombre"]] > 0:
                            vidas, ronda, puntuacion, tiempo_congelado_flag = usar_comodin(comodin, comodines_disponibles, vidas, ronda, puntuacion, tiempo_congelado_flag)
                            reproducir_sonido_func("comodin_usado", sonidos, estado_config, None)
                            selected_response = "comodin_usado"
                            respuesta_seleccionada = True
                            comodin_usado = True
                            break

                    if not comodin_usado and not respuesta_seleccionada:
                        for rect, respuesta in opcion_rects:
                            if rect.collidepoint(mouse_pos):
                                if respuesta == resultados[ecuaciones.index(ecuacion)]:
                                    reproducir_sonido_func("opcion_correcta", sonidos, estado_config, None)
                                    selected_response = "correcto"
                                else:
                                    if tiempo_restante > 0:
                                        vidas -= 1
                                        reproducir_sonido_func("opcion_incorrecta", sonidos, estado_config, None)
                                    selected_response = "incorrecto"
                                respuesta_seleccionada = True
                                break

            reloj.tick(30)

        if respuesta_seleccionada:
            return selected_response, vidas, ronda, puntuacion, tiempo_restante, tiempo_congelado_flag