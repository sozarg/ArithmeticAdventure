def usar_comodin(comodin, comodines_disponibles, vidas, ronda, puntuacion, tiempo_congelado_flag):
    """
    Aplica el efecto del comodín seleccionado y actualiza las variables del juego.
    
    Args:
        comodin (dict): Comodín a usar.
        comodines_disponibles (dict): Comodines disponibles.
        vidas (int): Número de vidas del jugador.
        ronda (int): Ronda actual.
        puntuacion (int): Puntuación del jugador.
        tiempo_congelado_flag (list): Bandera de tiempo congelado.
        
    Returns:
        tuple: Actualización de vidas, ronda, puntuación y bandera de tiempo congelado.
    """
    nombre = comodin["nombre"]
    if nombre == "ganar_vida":
        vidas += 1
    elif nombre == "congelar_tiempo":
        tiempo_congelado_flag[0] = True
    elif nombre == "ganar_ronda":
        puntuacion += 1
        ronda += 1
    comodines_disponibles[nombre] -= 1
    comodin["usado"] = True
    return vidas, ronda, puntuacion, tiempo_congelado_flag