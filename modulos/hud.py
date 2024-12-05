BLACK = (0, 0, 0)
RED = (255, 0, 0)

def dibujar_corazones(HEART_IMAGE, vidas, WIDTH, HEIGHT, screen):
    """
    Dibuja los corazones que representan las vidas del jugador en la esquina inferior derecha.
    
    Args:
        HEART_IMAGE (pygame.Surface): Imagen del corazón.
        vidas (int): Número de vidas.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        screen (pygame.Surface): Superficie de la pantalla.
    """
    heart_width, heart_height = HEART_IMAGE.get_size()
    margin_right = 80
    margin_bottom = 80
    espacio = 10

    for i in range(vidas):
        pos_x = WIDTH - margin_right - (i + 1) * (heart_width + espacio)
        pos_y = HEIGHT - margin_bottom - heart_height
        HEART_IMAGE_rect = HEART_IMAGE.get_rect(topleft=(pos_x, pos_y))
        screen.blit(HEART_IMAGE, HEART_IMAGE_rect)

def mostrar_hud(font, small_font, vidas, puntuacion, nivel, ronda, ecuacion, tiempo_restante, tiempo_congelado, HEART_IMAGE, ECUACION_BACKGROUND, WIDTH, HEIGHT, screen):
    """
    Muestra los elementos del HUD, incluyendo vidas, puntuación, nivel, ronda, tiempo y la ecuación actual.
    
    Args:
        font (pygame.font.Font): Fuente principal.
        small_font (pygame.font.Font): Fuente secundaria.
        vidas (int): Número de vidas.
        puntuacion (int): Puntuación del jugador.
        nivel (int): Nivel actual.
        ronda (int): Ronda actual.
        ecuacion (str): Ecuación actual.
        tiempo_restante (int): Tiempo restante.
        tiempo_congelado (bool): Estado de congelación del tiempo.
        HEART_IMAGE (pygame.Surface): Imagen del corazón.
        ECUACION_BACKGROUND (pygame.Surface): Imagen de fondo para la ecuación.
        WIDTH (int): Ancho de la pantalla.
        HEIGHT (int): Alto de la pantalla.
        screen (pygame.Surface): Superficie de la pantalla.
    """
    margen_lateral = 90
    margen_superior = 80

    dibujar_corazones(HEART_IMAGE, vidas, WIDTH, HEIGHT, screen)

    estado_ronda = small_font.render(f"Ronda: {ronda}/5", True, BLACK)
    estado_nivel = small_font.render(f"Nivel: {nivel}", True, BLACK)
    estado_puntuacion = small_font.render(f"Puntuación: {puntuacion}", True, BLACK)

    screen.blit(estado_ronda, (WIDTH - estado_ronda.get_width() - margen_lateral, margen_superior))
    screen.blit(estado_nivel, (WIDTH - estado_nivel.get_width() - margen_lateral, margen_superior + estado_ronda.get_height() + 5))
    screen.blit(estado_puntuacion, (WIDTH - estado_puntuacion.get_width() - margen_lateral, margen_superior + estado_ronda.get_height() + estado_nivel.get_height() + 10))

    if tiempo_congelado:
        estado_tiempo = small_font.render(f"Tiempo: {tiempo_restante}s (Congelado)", True, RED)
    else:
        estado_tiempo = small_font.render(f"Tiempo: {tiempo_restante}s", True, BLACK)
    screen.blit(estado_tiempo, ((WIDTH - estado_tiempo.get_width()) // 2, margen_superior))

    ecuacion_rect = ECUACION_BACKGROUND.get_rect(center=(WIDTH // 2, margen_superior + estado_tiempo.get_height() + 20 + ECUACION_BACKGROUND.get_height() // 2))
    screen.blit(ECUACION_BACKGROUND, ecuacion_rect.topleft)
    texto_ecuacion = font.render(f"{ecuacion}", True, BLACK)
    screen.blit(texto_ecuacion, (ecuacion_rect.centerx - texto_ecuacion.get_width() // 2, ecuacion_rect.centery - texto_ecuacion.get_height() // 2))
