import random
import time

def obtener_lista_niveles() -> dict:    
    with open("problemas.csv", "r", encoding="utf8") as problemas:
        problemas.readline()
        keys = {str(i): [[], []] for i in range(1, 6)}

        for linea in problemas:
            dificultad, ecuacion, resultado = linea.split(",")
            dificultad = dificultad.strip()
            resultado = int(resultado.strip())
            keys[dificultad][0].append(ecuacion.strip())
            keys[dificultad][1].append(resultado)
    return keys

def medir_tiempo_respuesta(funcion):
    inicio = time.time()
    resultado = funcion()
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    return resultado, tiempo_transcurrido

def obtener_respuesta_usuario() -> int:
    while True:
        try:
            return int(input("Tu respuesta: "))
        except ValueError:
            print("Error, número no ingresado.")

def ecuacion_correcta(vidas: int, puntuacion: int, control: int, cantidad_preguntas: int) -> tuple:
    puntuacion += 1
    control += 1
    if control < cantidad_preguntas:
        print(f"¡Correcto! Te quedan {cantidad_preguntas - control} preguntas.")
    return vidas, puntuacion, control

def ecuacion_incorrecta(vidas: int) -> int:
    vidas -= 1
    if vidas > 0:
        print(f"Te quedan {vidas} vidas.")
    else:
        print("Te quedaste sin vidas.")
    return vidas

def hacer_pregunta(ecuaciones, resultados) -> bool:
    indice = random.randint(0, len(ecuaciones) - 1)
    ecuacion_actual = ecuaciones[indice]
    resultado_actual = resultados[indice]

    print(f"Ecuación: {ecuacion_actual}")
    respuesta_usuario, tiempo_transcurrido = medir_tiempo_respuesta(obtener_respuesta_usuario)
    
    if tiempo_transcurrido > 10:
        print(f"¡Perdiste! Sobrepasaste los 10 segundos. La respuesta era: {resultado_actual}.")
        return False
    if respuesta_usuario == resultado_actual:
        return True
    else:
        print(f"Incorrecto. La respuesta correcta era {resultado_actual}")
        return False

def jugar_nivel(nivel, niveles, vidas: int, puntuacion: int) -> tuple:
    ecuaciones = niveles[str(nivel)][0]
    resultados = niveles[str(nivel)][1]
    control = 0
    cantidad_preguntas = 5
    while control < cantidad_preguntas and vidas > 0:
        respuesta_correcta = hacer_pregunta(ecuaciones, resultados)
        
        if respuesta_correcta:
            vidas, puntuacion, control = ecuacion_correcta(vidas, puntuacion, control, cantidad_preguntas)
        else:
            vidas = ecuacion_incorrecta(vidas)

        if vidas == 0:
            break

    if control == cantidad_preguntas:
        nivel_completado = True
    else:
        nivel_completado = False

    return nivel_completado, vidas, puntuacion

def iniciar_juego():
    niveles = obtener_lista_niveles()
    vidas = 3
    puntuacion = 0

    for nivel_actual in range(1, 6):
        print(f"\n--- Nivel {nivel_actual} --- \nTenes 10 segundos para responder.")
        nivel_completado, vidas, puntuacion = jugar_nivel(nivel_actual, niveles, vidas, puntuacion)

        if nivel_completado:
            print(f"¡Has completado el nivel {nivel_actual}!")
        else:
            print(f"No pudiste completar el nivel {nivel_actual}.")
            break

    print(f"\nJuego terminado. Puntuación final: {puntuacion} puntos.")

def mostrar_menu():
    while True:
        print("¡Bienvenido a Arithmetic Adventure!")
        print("1. Iniciar juego")
        print("2. Salir del juego")

        try:
            opcion = int(input("Selecciona una opción (1-2): "))
            if opcion == 1:
                iniciar_juego()
            elif opcion == 2:
                print("¡Gracias por jugar!")
                break
            else:
                print("Por favor, selecciona una opción válida.")
        except ValueError:
            print("Error, número no ingresado.")

if __name__ == "__main__":
    mostrar_menu()
