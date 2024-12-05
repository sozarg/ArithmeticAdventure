import pygame
import sys
from modulos.contorno import dibujar_texto_con_contorno

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

def mostrar_menu_volumen(font, small_font, screen, cambiar_fondo, OPCIONES_IMAGE, reproducir_sonido, sonidos, estado_config, guardar_config, GRAY, BLACK, WIDTH, HEIGHT):
    """
    Muestra el submenú de configuración de volumen con sliders para música y sonidos.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        small_font (pygame.font.Font): Fuente secundaria.
        screen (pygame.Surface): Superficie de la pantalla.
        cambiar_fondo (function): Función para cambiar el fondo.
        OPCIONES_IMAGE (pygame.Surface): Imagen para botones.
        reproducir_sonido (function): Función para reproducir sonidos.
        sonidos (dict): Diccionario de sonidos pre-cargados.
        estado_config (dict): Configuración actual del juego.
        guardar_config (function): Función para guardar la configuración.
        GRAY (tuple): Color gris.
        BLACK (tuple): Color negro.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
    """
    activo = True
    slider_music = False
    slider_sounds = False

    slider_width = 400
    slider_height = 20
    slider_music_pos = (WIDTH // 2 - slider_width // 2, HEIGHT // 2 - 100)
    slider_sounds_pos = (WIDTH // 2 - slider_width // 2, HEIGHT // 2)

    while activo:
        cambiar_fondo("modulos/assets/fondo_menu.png")
        
        dibujar_texto_con_contorno("Configuración de Volumen", font, WHITE, BLACK, WIDTH // 2 - font.size("Configuración de Volumen")[0] // 2, HEIGHT // 6, screen)

        barra_music, indicador_music = dibujar_slider("Música", slider_music_pos[0], slider_music_pos[1], slider_width, slider_height, estado_config["music_volume"], small_font, BLACK, GRAY, RED, screen)
        barra_sounds, indicador_sounds = dibujar_slider("Sonidos", slider_sounds_pos[0], slider_sounds_pos[1], slider_width, slider_height, estado_config["sounds_volume"], small_font, BLACK, GRAY, RED, screen)

        dibujar_texto_con_contorno("Música", small_font, WHITE, BLACK, slider_music_pos[0], slider_music_pos[1] - 40, screen)
        dibujar_texto_con_contorno("Sonidos", small_font, WHITE, BLACK, slider_sounds_pos[0], slider_sounds_pos[1] - 40, screen)

        volver_button_rect = OPCIONES_IMAGE.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(OPCIONES_IMAGE, volver_button_rect.topleft)
        dibujar_texto_con_contorno("Volver al Menú", small_font, WHITE, BLACK, volver_button_rect.centerx - small_font.size("Volver al Menú")[0] // 2, volver_button_rect.centery - small_font.get_height() // 2, screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_config(None, estado_config)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if indicador_music.collidepoint(mouse_pos):
                        slider_music = True
                    elif indicador_sounds.collidepoint(mouse_pos):
                        slider_sounds = True
                    elif volver_button_rect.collidepoint(mouse_pos):
                        reproducir_sonido("tocar_opcion", sonidos, estado_config, None)
                        activo = False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    slider_music = False
                    slider_sounds = False
                    
            if event.type == pygame.MOUSEMOTION:
                if slider_music:
                    mouse_x = event.pos[0]
                    new_volume = (mouse_x - slider_music_pos[0]) / slider_width
                    new_volume = max(0.0, min(1.0, new_volume))
                    estado_config["music_volume"] = new_volume
                    pygame.mixer.music.set_volume(estado_config["music_volume"])
                    guardar_config(estado_config, estado_config)

                if slider_sounds:
                    mouse_x = event.pos[0]
                    new_volume = (mouse_x - slider_sounds_pos[0]) / slider_width
                    new_volume = max(0.0, min(1.0, new_volume))
                    estado_config["sounds_volume"] = new_volume
                    for sonido in sonidos.values():
                        sonido.set_volume(estado_config["sounds_volume"])
                    guardar_config(estado_config, estado_config)

def dibujar_slider(label, x, y, width, height, valor, small_font, BLACK, GRAY, RED, screen):
    """
    Dibuja un slider para ajustar el volumen con una etiqueta.
    
    Args:
        label (str): Etiqueta del slider.
        x (int): Posición X del slider.
        y (int): Posición Y del slider.
        width (int): Ancho del slider.
        height (int): Alto del slider.
        valor (float): Valor actual del slider (0.0 a 1.0).
        small_font (pygame.font.Font): Fuente secundaria.
        BLACK (tuple): Color negro.
        GRAY (tuple): Color gris.
        RED (tuple): Color rojo.
        screen (pygame.Surface): Superficie de la pantalla.
        
    Returns:
        tuple: Rectángulos de la barra y del indicador.
    """
    texto = small_font.render(label, True, BLACK)
    screen.blit(texto, (x, y - 40))

    barra_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, GRAY, barra_rect)

    indicador_x = x + int(valor * width)
    indicador_rect = pygame.Rect(indicador_x - 10, y - 10, 20, height + 20)
    pygame.draw.rect(screen, RED, indicador_rect)

    return barra_rect, indicador_rect