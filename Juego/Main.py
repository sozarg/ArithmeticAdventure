import random
from modulos.puntaje import guardar_puntaje
from modulos.niveles import obtener_lista_niveles
from modulos.respuestas import ecuacion_correcta, ecuacion_incorrecta, hacer_pregunta

def jugar_nivel(nivel, niveles, vidas: int, puntuacion: int, comodines: dict) -> tuple:
    """
    Permite al jugador resolver un conjunto de ecuaciones correspondientes a un nivel del juego.

    Args:
        nivel (int): El nivel actual del juego.
        niveles (dict): Diccionario con los niveles y sus respectivas ecuaciones y resultados.
        vidas (int): Cantidad de vidas restantes del jugador.
        puntuacion (int): Puntuación acumulada del jugador.
        comodines (dict): Diccionario con los comodines disponibles del jugador.

    Returns:
        tuple: Un tupla con nivel completado (bool), vidas restantes (int) y puntuación acumulada (int).
    """
    ecuaciones = niveles[str(nivel)][0]
    resultados = niveles[str(nivel)][1]
    control = 0
    cantidad_preguntas = 5
    
    indices_aleatorios = random.sample(range(len(ecuaciones)), len(ecuaciones))
    ecuaciones_mezcladas = []
    resultados_mezclados = []

    for i in indices_aleatorios:
        ecuaciones_mezcladas.append(ecuaciones[i])
        resultados_mezclados.append(resultados[i])
    
    while control < cantidad_preguntas and vidas > 0:
        ecuacion_actual = ecuaciones_mezcladas[control]
        resultado_actual = resultados_mezclados[control]
        
        respuesta, tiempo_transcurrido = hacer_pregunta(ecuacion_actual, resultado_actual, comodines)
        
        if respuesta == "ganar":
            control += 1
            puntuacion += 1
            continue
        elif respuesta == "sumar_vida":
            vidas += 1
            print(f"Ahora tienes {vidas} vidas.")
            continue
        elif respuesta:
            vidas, puntuacion, control = ecuacion_correcta(vidas, puntuacion, control, cantidad_preguntas)
        else:
            vidas = ecuacion_incorrecta(vidas)
            ecuaciones_mezcladas.pop(control)
            resultados_mezclados.pop(control)

        if vidas == 0:
            break

    nivel_completado = control == cantidad_preguntas

    return nivel_completado, vidas, puntuacion

def iniciar_juego():
    """
    Inicia el juego solicitando el nombre del jugador y gestionando los niveles.

    Returns:
        None
    """
    nombre_jugador = input("Por favor, ingresa tu nombre: ")
    niveles = obtener_lista_niveles()
    vidas = 3
    puntuacion = 0
    comodines = {"joker1": 1, "joker2": 1, "joker3": 1}

    for nivel_actual in range(1, 6):
        print(f"\n--- Nivel {nivel_actual} --- \nTenes 10 segundos para responder.")
        nivel_completado, vidas, puntuacion = jugar_nivel(nivel_actual, niveles, vidas, puntuacion, comodines)

        if nivel_completado:
            print(f"¡Has completado el nivel {nivel_actual}!")
        else:
            print(f"No pudiste completar el nivel {nivel_actual}.")
            break

    print(f"\nJuego terminado. Puntuación final: {puntuacion} puntos.")
    guardar_puntaje(nombre_jugador, puntuacion)

def mostrar_menu():
    """
    Muestra el menú principal del juego y permite al jugador iniciar o salir del juego.

    Returns:
        None
    """
    while True:
        print("\n¡Bienvenido a Arithmetic Adventure!")
        print("1. Iniciar juego")
        print("2. Salir del juego")

        try:
            opcion = int(input("Selecciona una opción (1-2): "))
            if opcion == 1:
                iniciar_juego()
            elif opcion == 2:
                print("Gracias por jugar.")
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Error, número no ingresado.")

if __name__ == "__main__":
    mostrar_menu()
