"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo valores correctos
(por ejemplo, el radio no puede ser un número negativo) y si no es así que pida muestre un aviso y vuelva a pedir el valor.
"""

import math

# --- Funciones de cálculo ---
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

# --- Función para mostrar el menú ---
def mostrar_menu():
    print("\n1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

# --- Funciones para cada opción con validación ---
def opcion1():
    radio = -1
    while radio <= 0:
        radio = float(input("Introduce el radio del círculo: "))
        if radio <= 0:
            print("El radio debe ser mayor que 0.")
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")

def opcion2():
    base = -1
    altura = -1
    while base <= 0:
        base = float(input("Introduce la base del triángulo: "))
        if base <= 0:
            print("La base debe ser mayor que 0.")
    while altura <= 0:
        altura = float(input("Introduce la altura del triángulo: "))
        if altura <= 0:
            print("La altura debe ser mayor que 0.")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")

def opcion3():
    base = -1
    altura = -1
    while base <= 0:
        base = float(input("Introduce la base del rectángulo: "))
        if base <= 0:
            print("La base debe ser mayor que 0.")
    while altura <= 0:
        altura = float(input("Introduce la altura del rectángulo: "))
        if altura <= 0:
            print("La altura debe ser mayor que 0.")
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area:.2f}")

# --- Programa principal ---
opcion = 0
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Introduce una opción (1-4): "))

    match opcion:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            print("Saliendo del programa...")
        case _:
            print("Opción no válida. Intenta de nuevo.")
