matriz_a = [[1,5],
            [2,3],
            ]

matriz_b = []

filas = len(matriz_a)
columnas = len(matriz_a[0])

for j in range(columnas):
    fila_temp = []
    for i in range(filas):
        fila_temp.append(matriz_a[i][j])
    matriz_b.append(fila_temp)

print(matriz_b)        