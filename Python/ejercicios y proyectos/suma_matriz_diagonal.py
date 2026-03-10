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
            print(f"0{matrix[i][j]}", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()

x = -1
y = 0
suma_diagonal = 0

for _ in range(n):
    suma_diagonal += matrix[x][y]
    x -= 1
    y += 1

print(suma_diagonal)