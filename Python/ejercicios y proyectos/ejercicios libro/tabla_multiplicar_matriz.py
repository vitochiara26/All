matrix = []

for matriz_i in range(1,11):
    matrix.append([])
    for matriz_j in range(1,11):
        if matriz_i*matriz_j < 10:
            matrix[matriz_i-1].append(str(matriz_i) + " x " + str(matriz_j) + "  = " + str(matriz_i*matriz_j))
        elif matriz_j >= 10:
            matrix[matriz_i-1].append(str(matriz_i) + " x " + str(matriz_j) + " = " + str(matriz_i*matriz_j))
        else:
            matrix[matriz_i-1].append(str(matriz_i) + " x " + str(matriz_j) + "  = " + str(matriz_i*matriz_j))
    

for i in range(0,10):
    for j in range(1,4):
        f = len(matrix[-1][-1])-len(matrix[j][i])
        print(matrix[j][i], end=" "*f)
    print()
print()
for i in range(0,10):
    for j in range(4,7):
        f = len(matrix[-1][-1])-len(matrix[j][i])
        print(matrix[j][i], end=" "*f)
    print()
print()
for i in range(0,10):
    for j in range(7,10):
        f = len(matrix[-1][-1])-len(matrix[j][i])
        print(matrix[j][i], end=" "*f)
    print()