import threading


def preguntar():
    respuesta = input("¿Qué número es más grande, el 1 o el 2? Tienes 10 segundos: ")
    if respuesta.strip() == "2":
        print("¡Correcto! El número 2 es más grande.")
    else:
        print("Respuesta incorrecta. El número 2 es más grande.")

def tiempo_excedido():
    print("\n¡Tiempo agotado! El número 2 es más grande.")
    exit() 

timer = threading.Timer(10, tiempo_excedido)
timer.start()

preguntar()

timer.cancel()
