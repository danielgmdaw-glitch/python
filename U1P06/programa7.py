minutos_totales = int(input("Introduce la cantidad de minutos: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60

print(f"{minutos_totales} minutos corresponden a {horas} horas y {minutos} minutos.")