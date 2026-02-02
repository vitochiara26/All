n = int(input("Introduce el número N: "))

# Caso especial: si el número es 0, tiene 1 dígito
if n == 0:
    cantidad = 1
else:
    n = abs(n)
    cantidad = 0
    while n > 0:
        n //= 10  # División entera: elimina el último dígito
        cantidad += 1

print(f"El número de dígitos es: {cantidad}")