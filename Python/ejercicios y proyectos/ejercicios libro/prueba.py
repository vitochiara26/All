n = 3
m = 3
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

print(matrix)