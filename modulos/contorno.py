import pygame

def dibujar_texto_con_contorno(texto, font, color_texto, color_contorno, x, y, screen):
    """
    Dibuja un texto con contorno alrededor de él.
    
    Args:
        texto (str): El texto a dibujar.
        font (pygame.font.Font): La fuente del texto.
        color_texto (tuple): El color del texto.
        color_contorno (tuple): El color del contorno.
        x (int): Coordenada x para la posición del texto.
        y (int): Coordenada y para la posición del texto.
        screen (pygame.Surface): Superficie sobre la que dibujar.
    """

    texto_contorno = font.render(texto, True, color_contorno)
    for offset_x in [-2, 2]:  #nos desplazamos dos pixeles en el eje x
        for offset_y in [-2, 2]:  #nos desplazamos dos pixeles en el eje y
            screen.blit(texto_contorno, (x + offset_x, y + offset_y))

    texto_renderizado = font.render(texto, True, color_texto)
    screen.blit(texto_renderizado, (x, y))
