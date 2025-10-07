#Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación solicita genera un número aleatorio entre 1 y 20.
#A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
#El programa termina cuando se acierta el número.
#Puedes generar el número usando la función random.randrange(1, 21) para obtener un número aleatorio entre 1 y 20
#Mejora el programa de forma que el usuario tenga solo 3 intentos.

import random

numero_secreto = random.randrange(1, 21)
intentos = 3

while intentos > 0:
    num = int(input("Adivina el número (1-20): "))
    if num == numero_secreto:
        print("¡Correcto! Has acertado.")
        break
    elif num < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    intentos -= 1

if intentos == 0:
    print(f"Has perdido. El número era {numero_secreto}.")