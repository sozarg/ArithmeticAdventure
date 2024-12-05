import pygame
import sys
from modulos.guardar_datos import guardar_config
from modulos.contorno import dibujar_texto_con_contorno

def ingresar_nombre_usuario(font, small_font, screen, cambiar_fondo_func, WIDTH, HEIGHT, GRAY, BLACK):
    """
    Permite al jugador ingresar su nombre antes de iniciar el juego.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        small_font (pygame.font.Font): Fuente secundaria.
        screen (pygame.Surface): Superficie de la pantalla.
        cambiar_fondo_func (function): Función para cambiar el fondo.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        GRAY (tuple): Color gris.
        BLACK (tuple): Color negro.
        
    Returns:
        str: Nombre ingresado por el jugador.
    """
    cambiar_fondo_func("modulos/assets/fondo_nombre.png")
    nombre = ""
    activo = True

    while activo:
        cambiar_fondo_func("modulos/assets/fondo_nombre.png")

        dibujar_texto_con_contorno("Ingresa tu nombre:", font, (255, 255, 255), BLACK, WIDTH // 2 - font.size("Ingresa tu nombre:")[0] // 2, HEIGHT // 4, screen)

        cuadro_nombre = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 25, 300, 50)
        pygame.draw.rect(screen, GRAY, cuadro_nombre)

        dibujar_texto_con_contorno(nombre, font, (255, 255, 255), BLACK, cuadro_nombre.x + 10, cuadro_nombre.y + 5, screen)

        dibujar_texto_con_contorno("Presiona Enter para continuar.", small_font, (255, 255, 255), BLACK, WIDTH // 2 - small_font.size("Presiona Enter para continuar.")[0] // 2, HEIGHT // 2 + 100, screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_config(None, None)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and nombre.strip():
                    activo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    if event.unicode.isprintable():
                        nombre += event.unicode

    return nombre.strip()