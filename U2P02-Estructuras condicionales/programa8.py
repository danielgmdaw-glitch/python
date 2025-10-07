#Escribe un programa que simule un juego en el que dos jugadores tiran dos dados.
#El que saque mayor puntuación total, gana. Si la puntuación total coincide, 
# gana quien haya sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
#Puedes pedir el valor de cada tirada de dados por teclado o usar la la función random.randrange(1, 7) 
#para obtener un número aleatorio entre 1 y 6 (para ello debes poner import random al inicio del programa)
import random

print("Tirada del jugador 1:")
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
print(f"Dados jugador 1: {dado1_j1}, {dado2_j1} (total = {dado1_j1 + dado2_j1})")

print("\nTirada del jugador 2:")
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
print(f"Dados jugador 2: {dado1_j2}, {dado2_j2} (total = {dado1_j2 + dado2_j2})")

total_j1 = dado1_j1 + dado2_j1
total_j2 = dado1_j2 + dado2_j2

if total_j1 > total_j2:
    print("\nGana el jugador 1.")
elif total_j2 > total_j1:
    print("\nGana el jugador 2.")
else:
    # Empate en total, se compara el dado más alto
    max_j1 = max(dado1_j1, dado2_j1)
    max_j2 = max(dado1_j2, dado2_j2)
    if max_j1 > max_j2:
        print("\nGana el jugador 1 por tener el dado más alto.")
    elif max_j2 > max_j1:
        print("\nGana el jugador 2 por tener el dado más alto.")
    else:
        print("\nEmpate total.")