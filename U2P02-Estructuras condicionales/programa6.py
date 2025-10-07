#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

valida = True

# Comprobamos mes
if mes < 1 or mes > 12:
    valida = False
# Comprobamos días según el mes
elif mes in (1, 3, 5, 7, 8, 10, 12):
    if not (1 <= dia <= 31):
        valida = False
elif mes in (4, 6, 9, 11):
    if not (1 <= dia <= 30):
        valida = False
elif mes == 2: #no tenemos en cuenta los años bisiestos
    if dia < 1 or dia > 28:
        valida = False

if valida:
    print("La fecha es correcta.")
else:
    print("La fecha NO es correcta.")