# Programa que invierte un número de dos cifras
numero = int(input("Introduce un número de dos cifras: "))
decenas = numero // 10
unidades = numero % 10
numero_invertido = unidades * 10 + decenas
print(f"Número invertido: {numero_invertido}")