import time

def medir_tiempo_respuesta(funcion, congelar_tiempo=False) -> tuple:
    """
    Mide el tiempo que tarda el jugador en responder una pregunta, con la opción de congelar el tiempo.

    Args:
        funcion (function): Función que obtiene la respuesta del usuario.
        congelar_tiempo (bool): Indica si el tiempo debe ser congelado (sin límite).

    Returns:
        tuple: Respuesta del usuario y el tiempo transcurrido.
    """
    if congelar_tiempo:
        return funcion(), 0
    
    inicio = time.time()
    resultado = funcion()
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    return resultado, tiempo_transcurrido
