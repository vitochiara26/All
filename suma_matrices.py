matrix_uno = [[1,2,3],
              [4,5,6],
              [7,8,9]]

matrix_dos = [[9,8,7],
              [6,5,4],
              [3,2,1]]

matrix_tres = []

for row in range(len(matrix_uno)):
    nueva_fila = []
    for element in range(len(matrix_uno[0])):
        nueva_fila.append(matrix_uno[row][element] + matrix_dos[row][element])
    matrix_tres.append(nueva_fila)

for row in range(len(matrix_uno)):
    if row != 1:
        print(f"{matrix_uno[row]}   {matrix_dos[row]}   {matrix_tres[row]}")
    else:
        print(f"{matrix_uno[row]} + {matrix_dos[row]} = {matrix_tres[row]}")
