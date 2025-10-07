#Escribe un programa que lea por teclado un número real entre 1 y 10,
#simulando una nota numérica, y muestre un mensaje indicando la calificación obtenida 
#Si el número introducido no está en ninguno de los rangos anteriores debe mostrar 
#un mensaje de error indicando que la nota no es válida.
#Hay que usar la estructura match.
nota = float(input("Introduce una nota (0-10): "))

match nota:
    case _ if 0 <= nota < 5:
        print("Insuficiente")
    case _ if 5 <= nota < 6:
        print("Suficiente")
    case _ if 6 <= nota < 7:
        print("Bien")
    case _ if 7 <= nota < 9:
        print("Notable")
    case _ if 9 <= nota <= 10:
        print("Sobresaliente")
    case _:
        print("Error: la nota no es válida.")