import random
from modulos.opciones import generar_opciones
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def jugar_nivel(nivel, niveles, vidas, puntuacion, comodines_disponibles, comodines_obj, mostrar_hud_func, dibujar_comodines_func, dibujar_opciones_func, hacer_pregunta_func, reproducir_musica_func, cambiar_fondo_func, sonidos, reproducir_sonido_func, detener_musica_func, current_music, WIDTH, HEIGHT, screen, estado_config):
    """
    Maneja la lógica de un nivel completo, incluyendo rondas y manejo de vidas.
    
    Args:
        nivel (int): Número del nivel a jugar.
        niveles (dict): Diccionario de niveles con sus ecuaciones y resultados.
        vidas (int): Número de vidas del jugador.
        puntuacion (int): Puntuación del jugador.
        comodines_disponibles (dict): Comodines disponibles.
        comodines_obj (list): Lista de objetos de comodines.
        mostrar_hud_func (function): Función para mostrar el HUD.
        dibujar_comodines_func (function): Función para dibujar comodines.
        dibujar_opciones_func (function): Función para dibujar opciones de respuesta.
        hacer_pregunta_func (function): Función para manejar una pregunta.
        reproducir_musica_func (function): Función para reproducir música.
        cambiar_fondo_func (function): Función para cambiar el fondo.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        reproducir_sonido_func (function): Función para reproducir sonidos.
        detener_musica_func (function): Función para detener la música.
        current_music (list): Lista con el nombre actual y el volumen de la música.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        screen (pygame.Surface): Superficie de la pantalla.
        estado_config (dict): Configuración actual del juego.
        
    Returns:
        tuple: Éxito del nivel, actualización de vidas, puntuación y comodines disponibles.
    """
    reproducir_musica_func("modulos/assets/musica_juego.mp3", loop=-1, music_name="game", current_music_list=current_music)
    cambiar_fondo_func("modulos/assets/fondo_juego.png")

    ecuaciones = niveles[str(nivel)][0]
    resultados = niveles[str(nivel)][1]
    ronda = 1
    tiempo_limite = 10
    preguntas_usadas = set()
    seleccionar_nueva_pregunta = True
    tiempo_restante = tiempo_limite
    tiempo_congelado_flag = [False]

    while ronda <= 5 and vidas > 0:
        if seleccionar_nueva_pregunta:
            while True:
                if len(preguntas_usadas) >= len(ecuaciones):
                    preguntas_usadas = set()
                indice_random = random.randint(0, len(ecuaciones) - 1)
                
                encontrado = False
                for usado in preguntas_usadas:
                    if usado == indice_random:
                        encontrado = True
                        break
                
                if not encontrado:
                    preguntas_usadas.add(indice_random)
                    break
            
            ecuacion = ecuaciones[indice_random]
            respuesta_correcta = resultados[indice_random]
            opciones = generar_opciones(respuesta_correcta)
            seleccionar_nueva_pregunta = False
            tiempo_restante = tiempo_limite
            tiempo_congelado_flag = [False]
        
        respuesta, vidas, ronda, puntuacion, tiempo_restante, tiempo_congelado_flag = hacer_pregunta_func(
            ecuacion, opciones, vidas, puntuacion, nivel, ronda, tiempo_restante, comodines_disponibles, ecuaciones, resultados, tiempo_congelado_flag, comodines_obj,
            mostrar_hud_func, dibujar_comodines_func, dibujar_opciones_func, cambiar_fondo_func, sonidos, reproducir_sonido_func, BLACK, RED, WIDTH, HEIGHT, screen, estado_config
        )

        if respuesta == "ganar_ronda":
            seleccionar_nueva_pregunta = False

        elif respuesta == "correcto":
            puntuacion += 1
            ronda += 1
            seleccionar_nueva_pregunta = True
            tiempo_restante = tiempo_limite
            tiempo_congelado_flag = [False]

        elif respuesta == "comodin_usado":
            seleccionar_nueva_pregunta = False

        elif respuesta == "incorrecto" or respuesta == "tiempo_agotado":
            seleccionar_nueva_pregunta = True
            tiempo_congelado_flag = [False]

    if vidas <= 0:
        reproducir_sonido_func("pantalla_perder", sonidos, estado_config, None)
        detener_musica_func(current_music)
        return False, vidas, puntuacion, comodines_disponibles
    if nivel == 5:
        reproducir_sonido_func("pantalla_ganar", sonidos, estado_config, None)
        detener_musica_func(current_music)

    return True, vidas, puntuacion, comodines_disponibles
