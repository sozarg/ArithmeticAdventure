import random

def generar_opciones(respuesta_correcta):
    """
    Genera una lista de opciones de respuesta, incluyendo la correcta y tres incorrectas.

    Args:
        respuesta_correcta (int): Respuesta correcta de la ecuación.

    Returns:
        list: Lista de opciones de respuesta mezcladas.
    """
    opciones = [respuesta_correcta]
    while len(opciones) < 4:
        opcion_incorrecta = random.randint(max(1, respuesta_correcta - 5), respuesta_correcta + 5)
        existe = False
        for opcion in opciones:
            if opcion == opcion_incorrecta:
                existe = True
                break
        if not existe:
            opciones.append(opcion_incorrecta)
    random.shuffle(opciones)
    return opciones