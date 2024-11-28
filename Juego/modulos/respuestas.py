from modulos.tiempo import medir_tiempo_respuesta

def obtener_respuesta_usuario() -> str:
    """
    Obtiene la respuesta del usuario a una pregunta, permitiendo el uso de comodines.

    Returns:
        str: La respuesta ingresada por el usuario o el comodín elegido.
    """
    while True:
        respuesta = input("Tu respuesta: ")
        if respuesta.lower() in ["joker1", "joker2", "joker3"]:
            return respuesta.lower()
        try:
            return int(respuesta)
        except ValueError:
            print("Error, número no ingresado o comodín no válido.")

def ecuacion_correcta(vidas: int, puntuacion: int, control: int, cantidad_preguntas: int) -> tuple:
    """
    Gestiona la respuesta correcta del jugador, aumentando la puntuación y control de preguntas.

    Args:
        vidas (int): Cantidad de vidas restantes del jugador.
        puntuacion (int): Puntuación acumulada del jugador.
        control (int): Índice de la pregunta actual.
        cantidad_preguntas (int): Cantidad total de preguntas en el nivel.

    Returns:
        tuple: Vidas restantes (int), puntuación acumulada (int) y control de preguntas (int).
    """
    puntuacion += 1
    control += 1
    if control < cantidad_preguntas:
        print(f"¡Correcto! Te quedan {cantidad_preguntas - control} preguntas.")
    return vidas, puntuacion, control

def ecuacion_incorrecta(vidas: int) -> int:
    """
    Gestiona la respuesta incorrecta del jugador, reduciendo la cantidad de vidas restantes.

    Args:
        vidas (int): Cantidad de vidas restantes del jugador.

    Returns:
        int: Vidas restantes del jugador.
    """
    vidas -= 1
    if vidas > 0:
        print(f"Te quedan {vidas} vidas.")
    else:
        print("Te quedaste sin vidas.")
    return vidas

def hacer_pregunta(ecuacion_actual: str, resultado_actual: int, comodines: dict) -> tuple:
    """
    Realiza una pregunta al jugador y gestiona la respuesta, incluyendo el uso de comodines.

    Args:
        ecuacion_actual (str): Ecuación actual que se muestra al jugador.
        resultado_actual (int): Resultado correcto de la ecuación.
        comodines (dict): Diccionario con los comodines disponibles del jugador.

    Returns:
        tuple: Indica si la respuesta es correcta (bool o str) y el tiempo transcurrido (float).
    """
    print(f"Ecuación: {ecuacion_actual}")
    congelar_tiempo = False
    while True:
        respuesta_usuario, tiempo_transcurrido = medir_tiempo_respuesta(obtener_respuesta_usuario, congelar_tiempo)
        
        if isinstance(respuesta_usuario, str):
            if tiempo_transcurrido > 10:
                print(f"¡Perdiste! Sobrepasaste los 10 segundos. La respuesta era: {resultado_actual}.")
                return False, tiempo_transcurrido
            if respuesta_usuario == "joker1":
                if comodines["joker1"] > 0:
                    comodines["joker1"] -= 1
                    print("Comodín usado: Ganar ronda.")
                    return "ganar", tiempo_transcurrido
                else:
                    print("No te quedan más comodines de este tipo.")
            elif respuesta_usuario == "joker2":
                if comodines["joker2"] > 0:
                    comodines["joker2"] -= 1
                    print("Comodín usado: Congelar tiempo.")
                    congelar_tiempo = True
                else:
                    print("No te quedan más comodines de este tipo.")
            elif respuesta_usuario == "joker3":
                if comodines["joker3"] > 0:
                    comodines["joker3"] -= 1
                    print("Comodín usado: Sumar una vida.")
                    return "sumar_vida", tiempo_transcurrido
                else:
                    print("No te quedan más comodines de este tipo.")
        else:
            if tiempo_transcurrido > 10:
                print(f"¡Perdiste! Sobrepasaste los 10 segundos. La respuesta era: {resultado_actual}.")
                return False, tiempo_transcurrido
            if respuesta_usuario == resultado_actual:
                return True, tiempo_transcurrido
            else:
                print(f"Incorrecto. La respuesta correcta era {resultado_actual}")
                return False, tiempo_transcurrido
