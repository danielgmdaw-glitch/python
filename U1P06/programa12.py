# Programa que calcula la hora de llegada sumando N segundos
hh = int(input("Hora de salida (HH): "))
mm = int(input("Minutos de salida (MM): "))
ss = int(input("Segundos de salida (SS): "))
n = int(input("Tiempo de viaje en segundos: "))

# Convertimos todo a segundos
total_segundos = hh*3600 + mm*60 + ss + n

# Calculamos la nueva hora, minuto y segundo
llegada_hh = (total_segundos // 3600) % 24
llegada_mm = (total_segundos % 3600) // 60
llegada_ss = total_segundos % 60

#f → indica que es un número de punto flotante (float).
#.2 → indica que queremos 2 decimales después del punto.
print(f"Hora de llegada: {llegada_hh:02d}:{llegada_mm:02d}:{llegada_ss:02d}")