#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la suma y 
#la media de todos los números introducidos. Realiza dos versiones: una que utiliza la instrucción break y otra no.

# Versión 1: con break
suma = 0
contador = 0
while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    print("Suma:", suma)
    print("Media:", suma / contador)
else:
    print("No se introdujeron números.")

# Versión 2: sin break
suma = 0
contador = 0
num = -1
while num != 0:
    num = int(input("Introduce un número (0 para terminar): "))
    if num != 0:
        suma += num
        contador += 1

if contador > 0:
    print("Suma:", suma)
    print("Media:", suma / contador)
else:
    print("No se introdujeron números.")