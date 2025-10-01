# Programa que calcula la calificación final de un módulo
ra1 = float(input("Calificación RA1 (20%): "))
ra2 = float(input("Calificación RA2 (60%): "))
ra3 = float(input("Calificación RA3 (20%): "))

nota_final = ra1*0.2 + ra2*0.6 + ra3*0.2
print(f"Calificación final del módulo: {nota_final:.2f}")