# Programa que calcula el total con un 15% de descuento
total_compra = float(input("Introduce el total de la compra: "))
descuento = total_compra * 0.15
total_final = total_compra - descuento
print(f"Total a pagar con descuento: {total_final:.2f} €")