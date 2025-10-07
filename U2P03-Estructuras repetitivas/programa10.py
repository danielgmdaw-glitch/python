#Modifica el programa anterior par que pida en primer lugar el número de jugadores que van a jugar.
#Cada jugador irá jugando y el programa mostrará si ha ganado o no a la banca.

import random

num_jugadores = int(input("¿Cuántos jugadores van a jugar? "))
banca = random.randint(17, 21)
print(f"\nLa banca tiene {banca} puntos.\n")

for j in range(1, num_jugadores + 1):
    print(f"--- Jugador {j} ---")
    jugador = 0
    seguir = "s"

    while seguir.lower() == "s":
        carta = random.randint(1, 12)
        jugador += carta
        print(f"Has sacado un {carta}. Total: {jugador}")

        if jugador > 21:
            print("Te pasaste de 21. Pierdes.")
            break

        seguir = input("¿Quieres sacar otra carta? (s/n): ")

    if jugador <= 21:
        if jugador > banca:
            print("¡Has ganado a la banca!")
        else:
            print("Has perdido contra la banca.")
    print()
