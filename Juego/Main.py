import random

def obtener_lista_niveles() -> dict:
    with open("problemas.csv", "r", encoding = "utf8") as problemas:
        problemas.readline()
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

#funcion | dentro del nivel seleccionar un ejercicio random

resultado = obtener_lista_niveles()
print(resultado)