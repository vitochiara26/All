arreglo_a = [1, 4, 6, 9, 11]
arreglo_b = [2, 5, 10, 12]
arreglo_c = []

i = 0 # Puntero para arreglo_a
j = 0 # Puntero para arreglo_b

# Mientras ambos arreglos tengan elementos por comparar
while i < len(arreglo_a) and j < len(arreglo_b):
    if arreglo_a[i] < arreglo_b[j]:
        arreglo_c.append(arreglo_a[i])
        i += 1
    else:
        arreglo_c.append(arreglo_b[j])
        j += 1

# Si quedaron elementos en A (porque B se acabó primero)
while i < len(arreglo_a):
    arreglo_c.append(arreglo_a[i])
    i += 1

# Si quedaron elementos en B (porque A se acabó primero)
while j < len(arreglo_b):
    arreglo_c.append(arreglo_b[j])
    j += 1

print("Arreglo A:", arreglo_a)
print("Arreglo B:", arreglo_b)
print("Resultado ordenado C:", arreglo_c)