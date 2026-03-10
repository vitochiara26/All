n = 66
m = 66
matrix = []
for i in range(n):
    matrix.append([0]*m)

num = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1
        if matrix[i][j] < 10:
            print(f"0{matrix[i][j]}", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()

mod_n = int(input(f"Ingrese el numero de fila que desea modificar (1 a {n}): "))-1
mod_m = int(input(f"Ingrese el numero de columna que desea modificar (1 a {m}): "))-1
mod = int(input("Ingrese el valor a ingresar en esa posicion: "))

matrix[mod_n][mod_m] = mod

for i in range(n):
    for j in range(m):
        if matrix[i][j] < 10 and matrix[i][j] > 0:
            print(f"0{matrix[i][j]}", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
