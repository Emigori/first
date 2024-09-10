import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de números!")
    print("He generado un número secreto entre 1 y 100.")
    print("Intenta adivinar cuál es.")

    while not adivinado:
        intento = int(input("Introduce tu intento: "))

        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número secreto que era {numero_secreto}.")
            adivinado = True

# Llamamos a la función para iniciar el juego
adivina_el_numero()