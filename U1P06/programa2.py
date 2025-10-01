# Crear una variable con el número entero 6
a = 6

# Mostrar el tipo del objeto y de la variable (apuntan al mismo tipo)
print("Valor de a:", a)
print("Tipo del objeto:", type(6))
print("Tipo al que apunta la variable a:", type(a))

# Crear otra variable que apunte al mismo objeto
b = a

# Mostrar de nuevo los tipos
print("\nValor de b:", b)
print("Tipo del objeto:", type(6))
print("Tipo al que apunta la variable b:", type(b))

# Comprobar si apuntan al mismo objeto
print("\n¿a es b?", a is b)
print("¿a no es b?", a is not b)

# Asignar la cadena "Hola" a la primera variable
a = "Hola"

# Mostrar tipos después del cambio
print("\nValor de a:", a)
print("Tipo del objeto:", type("Hola"))
print("Tipo al que apunta la variable a:", type(a))

# Comprobación con isinstance
print("\n¿a es int?", isinstance(a, int))
print("¿a es str?", isinstance(a, str))
print("¿b es int?", isinstance(b, int))
print("¿b es str?", isinstance(b, str))
