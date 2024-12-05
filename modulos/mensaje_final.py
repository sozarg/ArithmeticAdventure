import pygame
import sys
from modulos.guardar_datos import guardar_puntaje
from modulos.config_volumen import reproducir_musica
from modulos.cargar_datos import cargar_config

def mostrar_mensaje_final(font, screen, cambiar_fondo_func, reproducir_sonido_func, sonidos, nombre, vidas, puntuacion, detener_musica_func, current_music, WIDTH, HEIGHT, WHITE, YELLOW, RED, BLACK):
    """
    Muestra el mensaje final al completar el juego, indicando si el jugador ganó o perdió.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        screen (pygame.Surface): Superficie de la pantalla.
        cambiar_fondo_func (function): Función para cambiar el fondo.
        reproducir_sonido_func (function): Función para reproducir sonidos.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        nombre (str): Nombre del jugador.
        vidas (int): Número de vidas restantes.
        puntuacion (int): Puntuación final del jugador.
        detener_musica_func (function): Función para detener la música.
        current_music (list): Lista con el nombre actual y el volumen de la música.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        WHITE (tuple): Color blanco.
        YELLOW (tuple): Color amarillo.
        RED (tuple): Color rojo.
        BLACK (tuple): Color negro.
    """
    estado_config = cargar_config()  # Cargar la configuración desde el archivo JSON

    if estado_config is None:
        print("Error: No se pudo cargar la configuración.")
        pygame.quit()
        sys.exit()
    guardar_puntaje(nombre, puntuacion)
    cambiar_fondo_func("modulos/assets/fondo_final.png")
    screen.fill(WHITE)

    if vidas > 0:
        mensaje_final = font.render("¡Felicidades! Has completado el juego.", True, YELLOW)
        reproducir_sonido_func("pantalla_ganar", sonidos, estado_config, None)
    else:
        mensaje_final = font.render("¡Game Over! Intenta nuevamente.", True, RED)
        reproducir_sonido_func("pantalla_perder", sonidos, estado_config, None)

    screen.blit(mensaje_final, ((WIDTH - mensaje_final.get_width()) // 2, HEIGHT // 2 - 50))

    mensaje_puntaje = font.render(f"Tu puntaje: {puntuacion} puntos", True, BLACK)
    screen.blit(mensaje_puntaje, ((WIDTH - mensaje_puntaje.get_width()) // 2, HEIGHT // 2 + 20))

    pygame.display.update()
    pygame.time.wait(3000)

    reproducir_musica("modulos/assets/musica_menu.mp3", loop=-1, music_name="menu", current_music=current_music)
