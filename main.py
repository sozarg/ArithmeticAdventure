import pygame
import sys

from modulos.cargar_datos import cargar_config, cargar_imagen, cargar_comodines, cargar_problemas
from modulos.guardar_datos import guardar_config
from modulos.config_volumen import reproducir_musica, reproducir_sonido, detener_musica
from modulos.botones import dibujar_comodines, dibujar_opciones
from modulos.hud import mostrar_hud
from modulos.nombre_usuario import ingresar_nombre_usuario
from modulos.logica_pregunta import hacer_pregunta
from modulos.logica_nivel import jugar_nivel
from modulos.mensaje_final import mostrar_mensaje_final
from modulos.mostrar_tabla import mostrar_tabla_puntuaciones
from modulos.mostrar_volumen import mostrar_menu_volumen
from modulos.menu import mostrar_menu

def main():
    """
    Función principal que inicializa Pygame, carga recursos, y muestra el menú principal.
    """
    global screen, estado_config, sonidos, BLACK, RED

    pygame.init()
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arithmetic Adventure")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    YELLOW = (255, 255, 0)
    BROWN = (139, 69, 19)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    RED = (255, 0, 0)

    estado_config = cargar_config()
    
    def guardar_config_func(config, estado_config_inner):
        guardar_config(config, estado_config_inner)

    try:
        font = pygame.font.Font("modulos/assets/Crang.ttf", 40)
        small_font = pygame.font.Font("modulos/assets/Crang.ttf", 30)
    except FileNotFoundError:
        font = pygame.font.SysFont("Arial", 40)
        small_font = pygame.font.SysFont("Arial", 30)

    HEART_IMAGE = cargar_imagen("modulos/assets/contador_vidas.png", (50, 50), GRAY)
    OPCIONES_IMAGE = cargar_imagen("modulos/assets/opciones.png", (200, 50), GRAY)
    ECUACION_BACKGROUND = cargar_imagen("modulos/assets/ecuacion.png", (350, 150), GRAY)

    pygame.mixer.init()

    sonidos = {
        "pantalla_ganar": pygame.mixer.Sound("modulos/assets/pantalla_ganar.mp3"),
        "pantalla_perder": pygame.mixer.Sound("modulos/assets/pantalla_perder.mp3"),
        "opcion_correcta": pygame.mixer.Sound("modulos/assets/opcion_correcta.mp3"),
        "comodin_usado": pygame.mixer.Sound("modulos/assets/comodin_usado.mp3"),
        "opcion_incorrecta": pygame.mixer.Sound("modulos/assets/opcion_incorrecta.mp3"),
        "tocar_opcion": pygame.mixer.Sound("modulos/assets/tocar_opcion.mp3")
    }

    for sonido in sonidos.values():
        sonido.set_volume(estado_config["sounds_volume"])

    SONIDO_CANAL = pygame.mixer.Channel(1)
    pygame.mixer.music.set_volume(estado_config["music_volume"])

    current_music = [None, estado_config["music_volume"]]

    rutas_comodines = {
        "ganar_vida": "modulos/assets/comodin_vidas.png",
        "congelar_tiempo": "modulos/assets/comodin_congelar.png",
        "ganar_ronda": "modulos/assets/comodin_ganar_ronda.png",
        "usado": "modulos/assets/comodin_usado.png"
    }

    niveles = cargar_problemas()

    def reproducir_sonido_func(nombre, sonidos_dict, config, canal):
        reproducir_sonido(nombre, sonidos_dict, config, SONIDO_CANAL)

    def reproducir_musica_func(ruta, loop, music_name, current_music_list):
        reproducir_musica(ruta, loop, music_name, current_music_list)

    def detener_musica_func(current_music_list):
        detener_musica(current_music_list)

    def cambiar_fondo_func(ruta):
        try:
            fondo = pygame.image.load(ruta).convert()
            fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
            screen.blit(fondo, (0, 0))
        except pygame.error as e:
            print(f"Error al cargar fondo {ruta}: {e}")
            screen.fill(WHITE)

    def mostrar_hud_func(vidas, puntuacion, nivel, ronda, ecuacion, tiempo_restante, tiempo_congelado):
        mostrar_hud(font, small_font, vidas, puntuacion, nivel, ronda, ecuacion, tiempo_restante, tiempo_congelado, HEART_IMAGE, ECUACION_BACKGROUND, WIDTH, HEIGHT, screen)

    def dibujar_comodines_func(comodines, comodines_disponibles, screen_inner, width_inner, height_inner):
        dibujar_comodines(comodines, comodines_disponibles, screen_inner, width_inner, height_inner)

    def dibujar_opciones_func(opciones, background_image, small_font_inner, width_inner, color_inner, screen_inner):
        return dibujar_opciones(opciones, background_image, small_font_inner, width_inner, color_inner, screen_inner)

    def hacer_pregunta_func(ecuacion, opciones, vidas, puntuacion, nivel, ronda, tiempo_restante, comodines_disponibles, ecuaciones, resultados, tiempo_congelado_flag, comodines_obj, mostrar_hud_f, dibujar_comodines_f, dibujar_opciones_f, cambiar_fondo_f, sonidos_dict, reproducir_sonido_f, BLACK_color, RED_color, width_inner, height_inner, screen_inner, config_inner):
        return hacer_pregunta(ecuacion, opciones, vidas, puntuacion, nivel, ronda, tiempo_restante, comodines_disponibles, ecuaciones, resultados, tiempo_congelado_flag, comodines_obj, mostrar_hud_f, dibujar_comodines_f, dibujar_opciones_f, cambiar_fondo_f, sonidos_dict, reproducir_sonido_f, BLACK_color, RED_color, width_inner, height_inner, screen_inner, config_inner)

    
    def inicializar_comodines():
        """
        Inicializa los comodines disponibles al inicio del juego.
        
        Returns:
            dict: Comodines disponibles con su cantidad inicial.
        """
        return {"ganar_vida": 1, "congelar_tiempo": 1, "ganar_ronda": 1}

    def iniciar_juego_func():
        nombre_jugador = ingresar_nombre_usuario(font, small_font, screen, cambiar_fondo_func, WIDTH, HEIGHT, GRAY, BLACK)
        vidas = 3
        puntuacion = 0
        comodines_disponibles = inicializar_comodines()
        comodines_obj = cargar_comodines(rutas_comodines, GRAY)

        for nivel in range(1, 6):
            exito, vidas, puntuacion, comodines_disponibles = jugar_nivel(
                nivel, niveles, vidas, puntuacion, comodines_disponibles, comodines_obj,
                mostrar_hud_func, dibujar_comodines_func, dibujar_opciones_func, hacer_pregunta_func,
                reproducir_musica_func, cambiar_fondo_func, sonidos, reproducir_sonido_func,
                detener_musica_func, current_music, WIDTH, HEIGHT, screen, estado_config
            )
            if not exito:
                break

        mostrar_mensaje_final(font, screen, cambiar_fondo_func, reproducir_sonido_func, sonidos, nombre_jugador, vidas, puntuacion, detener_musica_func, current_music, WIDTH, HEIGHT, WHITE, YELLOW, RED, BLACK)

    def mostrar_tabla_puntuaciones_func():
        mostrar_tabla_puntuaciones(font, small_font, screen, cambiar_fondo_func, OPCIONES_IMAGE, reproducir_sonido_func, sonidos, WIDTH, HEIGHT, BLACK, GOLD, SILVER, BROWN)

    def mostrar_menu_volumen_func():
        mostrar_menu_volumen(font, small_font, screen, cambiar_fondo_func, OPCIONES_IMAGE, reproducir_sonido_func, sonidos, estado_config, guardar_config_func, GRAY, BLACK, WIDTH, HEIGHT)

    mostrar_menu(font, small_font, screen, cambiar_fondo_func, OPCIONES_IMAGE, reproducir_sonido_func, iniciar_juego_func, mostrar_tabla_puntuaciones_func, mostrar_menu_volumen_func, reproducir_musica_func, sonidos, estado_config, guardar_config_func, BLACK, WIDTH, HEIGHT)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()