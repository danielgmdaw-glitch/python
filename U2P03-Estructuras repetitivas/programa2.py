#Escribe un que lea por teclado un número comprendido entre 1 y 10.
#No se dejara de pedir el número hasta que no se introduzca correctamente.
num = 0
while num < 1 or num > 10:
    num = int(input("Introduce un número entre 1 y 10: "))
print("Número correcto:", num)
