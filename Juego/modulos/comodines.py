# comodines.py

# Variables para manejar la cantidad de usos de cada comodín
cantidad_comodin_vidas = 1
cantidad_comodin_pregunta = 1
cantidad_comodin_tiempo = 1

# Función para mostrar los comodines disponibles
def mostrar_comodines():
    print("\nComodines disponibles:")
    print(f"a. Cambiar pregunta: {cantidad_comodin_pregunta} usos restantes")
    print(f"b. Recuperar vida: {cantidad_comodin_vidas} usos restantes")
    print(f"c. Congelar tiempo: {cantidad_comodin_tiempo} usos restantes")

# Función para usar el comodín "Cambiar pregunta"
def usar_comodin_cambiar_pregunta():
    global cantidad_comodin_pregunta
    if cantidad_comodin_pregunta > 0:
        cantidad_comodin_pregunta -= 1  # Restamos 1 al comodín de cambiar pregunta
        print("Comodín 'Cambiar pregunta' usado.")
        return True
    else:
        print("No puedes usar el comodín 'Cambiar pregunta' porque no tienes usos restantes.")
        return False

# Función para usar el comodín "Recuperar vida"
def usar_comodin_recuperar_vida(vidas):
    global cantidad_comodin_vidas
    if cantidad_comodin_vidas > 0:
        cantidad_comodin_vidas -= 1  # Restamos 1 al comodín de recuperar vida
        print("Comodín 'Recuperar vida' usado.")
        if vidas < 3:  # Solo sumamos una vida si no tienes el máximo de vidas
            vidas += 1
            print(f"Has recuperado una vida. Ahora tienes {vidas} vidas.")
        return vidas  # Devolvemos las vidas actualizadas
    else:
        print("No puedes usar el comodín 'Recuperar vida' porque no tienes usos restantes.")
        return vidas

# Función para usar el comodín "Congelar tiempo"
def usar_comodin_congelar_tiempo():
    global cantidad_comodin_tiempo
    if cantidad_comodin_tiempo > 0:
        cantidad_comodin_tiempo -= 1  # Restamos 1 al comodín de congelar tiempo
        print("Comodín 'Congelar tiempo' usado.")
        return True
    else:
        print("No puedes usar el comodín 'Congelar tiempo' porque no tienes usos restantes.")
        return False
