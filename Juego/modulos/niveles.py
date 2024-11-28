def obtener_lista_niveles() -> dict:
    """
    Obtiene la lista de niveles con sus respectivas ecuaciones y resultados desde un archivo CSV.

    Returns:
        dict: Un diccionario con los niveles y sus respectivas ecuaciones y resultados.
    """
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
