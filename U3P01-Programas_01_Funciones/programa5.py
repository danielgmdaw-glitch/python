"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables en Python (globales, no locales y locales).
"""
# Variable global
contador_global = 0

def funcion_local():
    # Variable local
    contador_local = 10
    print("Dentro de funcion_local, contador_local =", contador_local)
    
def funcion_global():
    global contador_global  # Indicamos que queremos usar la variable global
    contador_global += 1
    print("Dentro de funcion_global, contador_global =", contador_global)

def funcion_no_local():
    contador_externo = 5  # Variable local de funcion_no_local
    
    def funcion_interna():
        nonlocal contador_externo  # Usamos la variable de la función contenedora
        contador_externo += 5
        print("Dentro de funcion_interna, contador_externo =", contador_externo)
    
    print("Antes de llamar a funcion_interna, contador_externo =", contador_externo)
    funcion_interna()
    print("Después de llamar a funcion_interna, contador_externo =", contador_externo)

# --- Pruebas ---
print("Valor inicial de contador_global:", contador_global)

funcion_local()  # Solo afecta a su variable local
funcion_global()  # Modifica la variable global
funcion_no_local()  # Modifica una variable no local dentro de la función anidada

print("Valor final de contador_global:", contador_global)
