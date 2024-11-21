import random

# Función para leer el archivo CSV y obtener las ecuaciones por nivel
def obtener_lista_niveles() -> dict:
    with open("problemas.csv", "r", encoding="utf8") as problemas:
        problemas.readline()  # Ignorar la primera línea del archivo
        keys = {
            "1": [[], []],
            "2": [[], []],
            "3": [[], []],
            "4": [[], []],
            "5": [[], []]
        }

        for linea in problemas:
            dificultad, ecuacion, resultado = linea.split(",")
            dificultad = dificultad.strip()
            resultado = int(resultado.strip())
            keys[dificultad][0].append(ecuacion.strip())
            keys[dificultad][1].append(resultado)
    return keys

# Función para mostrar una ecuación aleatoria y verificar la respuesta
def hacer_pregunta(ecuaciones, resultados):
    indice = random.randint(0, len(ecuaciones) - 1)  # Seleccionar una ecuación aleatoria
    ecuacion_actual = ecuaciones[indice]
    resultado_actual = resultados[indice]
    
    print(f"\nEcuación: {ecuacion_actual}")
    try:
        respuesta_usuario = int(input("Tu respuesta: "))
        if respuesta_usuario == resultado_actual:
            print("¡Correcto!")
            return True
        else:
            print(f"Incorrecto. La respuesta correcta era {resultado_actual}")
            return False
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return False

# Función para jugar un nivel
def jugar_nivel(nivel, niveles):
    ecuaciones = niveles[str(nivel)][0]
    resultados = niveles[str(nivel)][1]
    vidas = 3  # Iniciar con 3 vidas
    puntuacion = 0
    cantidad_preguntas = 5  # Queremos 5 preguntas para pasar de nivel

    # Realizar preguntas hasta que el jugador complete 5 preguntas o pierda todas las vidas
    while puntuacion < cantidad_preguntas and vidas > 0:
        if hacer_pregunta(ecuaciones, resultados):
            puntuacion += 1
        else:
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")

    # Verificar si el jugador completó el nivel
    if puntuacion == cantidad_preguntas:
        print(f"\n¡Felicidades! Has completado el nivel {nivel} con {vidas} vidas restantes.")
        return True
    else:
        print(f"\nTe quedaste sin vidas o no completaste las 5 preguntas. Fin del nivel {nivel}.")
        return False

# Función para mostrar el menú y permitir al jugador seleccionar el nivel
def mostrar_menu():
    print("¡Bienvenido al juego de matemáticas!")
    print("Selecciona un nivel de dificultad:")
    print("1. Nivel 1 (Suma)")
    print("2. Nivel 2 (Resta)")
    print("3. Nivel 3 (Multiplicación)")
    print("4. Nivel 4 (División)")
    print("5. Nivel 5 (Operaciones combinadas)")

    while True:
        try:
            nivel = int(input("Selecciona el nivel (1-5): "))
            if 1 <= nivel <= 5:
                break
            else:
                print("Por favor, selecciona un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    niveles = obtener_lista_niveles()

    # Jugar mientras el jugador pase cada nivel
    for i in range(nivel, 6):
        print(f"\n--- Nivel {i} ---")
        if not jugar_nivel(i, niveles):
            print("El juego ha terminado.")
            break

if __name__ == "__main__":
    mostrar_menu()
