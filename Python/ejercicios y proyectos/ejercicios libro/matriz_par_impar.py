n = 4
matrix = []
for i in range(n):
    matrix.append([0]*n)

num = 1
for i in range(n):
    for j in range(n):
        matrix[i][j] = num
        num += 1
        if matrix[i][j] < 10:
            print(f"{matrix[i][j]} ", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()

pares = ""
impares = ""
for i in range(n):
    for j in range(n):
        if matrix[i][j] % 2 == 0:
            pares = pares + str(matrix[i][j]) + ", "
        else :
            impares = impares + str(matrix[i][j]) + ", "

pares = pares.strip(", ")
impares = impares.strip(", ")

print(f"\nElementos pares de la mattriz: {pares}")
print(f"Elementos impares de la mattriz: {impares}")
