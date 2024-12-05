import pygame
import sys

from modulos.contorno import dibujar_texto_con_contorno

def mostrar_menu(font, small_font, screen, cambiar_fondo_func, OPCIONES_IMAGE, reproducir_sonido_func, iniciar_juego_func, mostrar_tabla_puntuaciones_func, mostrar_menu_volumen_func, reproducir_musica_func, sonidos, estado_config, guardar_config_func, BLACK, WIDTH, HEIGHT):
    """
    Muestra el menú principal del juego con opciones para iniciar, ver puntuaciones, ajustar volumen y salir.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        small_font (pygame.font.Font): Fuente secundaria.
        screen (pygame.Surface): Superficie de la pantalla.
        cambiar_fondo_func (function): Función para cambiar el fondo.
        OPCIONES_IMAGE (pygame.Surface): Imagen para botones.
        reproducir_sonido_func (function): Función para reproducir sonidos.
        iniciar_juego_func (function): Función para iniciar el juego.
        mostrar_tabla_puntuaciones_func (function): Función para mostrar la tabla de puntuaciones.
        mostrar_menu_volumen_func (function): Función para mostrar el menú de volumen.
        reproducir_musica_func (function): Función para reproducir música.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        estado_config (dict): Configuración actual del juego.
        guardar_config_func (function): Función para guardar la configuración.
        BLACK (tuple): Color negro.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
    """
    reproducir_musica_func("modulos/assets/musica_menu.mp3", loop=-1, music_name="menu", current_music_list=[None, estado_config["music_volume"]])

    while True:
        cambiar_fondo_func("modulos/assets/fondo_menu.png")
        
        dibujar_texto_con_contorno("Arithmetic Adventure", font, (255, 255, 0), BLACK, (WIDTH - font.size("Arithmetic Adventure")[0]) // 2, HEIGHT // 6, screen)

        start_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        tabla_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        volumen_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        exit_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

        screen.blit(OPCIONES_IMAGE, start_button_rect.topleft)
        screen.blit(OPCIONES_IMAGE, tabla_button_rect.topleft)
        screen.blit(OPCIONES_IMAGE, volumen_button_rect.topleft)
        screen.blit(OPCIONES_IMAGE, exit_button_rect.topleft)

        for texto, rect in [
            (("Iniciar Juego", start_button_rect)),
            (("Tabla de Puntuaciones", tabla_button_rect)),
            (("Volumen", volumen_button_rect)),
            (("Salir", exit_button_rect))
        ]:
            dibujar_texto_con_contorno(texto, small_font, (255, 255, 255), BLACK, rect.centerx - small_font.size(texto)[0] // 2, rect.centery - small_font.get_height() // 2, screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_config_func(None, estado_config)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if start_button_rect.collidepoint(mouse_pos):
                        reproducir_sonido_func("tocar_opcion", sonidos, estado_config, None)
                        iniciar_juego_func()
                    elif tabla_button_rect.collidepoint(mouse_pos):
                        reproducir_sonido_func("tocar_opcion", sonidos, estado_config, None)
                        mostrar_tabla_puntuaciones_func()
                    elif volumen_button_rect.collidepoint(mouse_pos):
                        reproducir_sonido_func("tocar_opcion", sonidos, estado_config, None)
                        mostrar_menu_volumen_func()
                    elif exit_button_rect.collidepoint(mouse_pos):
                        reproducir_sonido_func("tocar_opcion", sonidos, estado_config, None)
                        guardar_config_func(estado_config, estado_config)
                        pygame.quit()
                        sys.exit()