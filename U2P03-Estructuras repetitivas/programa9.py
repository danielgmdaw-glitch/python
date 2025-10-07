#Escribe un programa para jugar a una versión muy simplificada del black jack. En primer lugar el ordenador 
#obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A continuación el jugador ira sacando cartas (con valores entre 1 y 5), 
#que se irán sumando para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una puntuación igual 
# o menor que la banca pierde, y si obtiene una puntuación superior a la banca gana.

import random

banca = random.randint(17, 21)
print(f"La banca tiene {banca} puntos.")

jugador = 0
seguir = "s"

while seguir.lower() == "s":
    carta = random.randint(1, 5)
    jugador += carta
    print(f"Has sacado un {carta}. Total: {jugador}")

    if jugador > 21:
        print("Te pasaste de 21. Pierdes.")
        break

    seguir = input("¿Quieres sacar otra carta? (s/n): ")

if jugador <= 21:
    if jugador > banca:
        print("¡Has ganado!")
    else:
        print("Has perdido contra la banca.")
