#Escribe un programa en Python que simule el juego de piedra, papel o tijera. 
#En primer lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle qué opción desea elegir.
#Después de leer la opción seleccionada por el usuario el programa generará un número aleatorio para simular una jugada y 
#mostrará un mensaje indicando si el usuario ha ganado o ha perdido dependiendo del resultado.
import random

print("Juego: Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

usuario = int(input("Elige una opción (1, 2 o 3): "))
pc = random.randint(1, 3)

# Mostrar elecciones
print(f"Tú elegiste: {usuario}")
print(f"La computadora eligió: {pc}")

# Determinar resultado
if usuario == pc:
    print("Empate.")
elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
    print("¡Has ganado!")
else:
    print("Has perdido.")
