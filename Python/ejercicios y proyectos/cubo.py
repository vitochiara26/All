n = 2
cubo = []

for i in range(n):
    cubo.append([])
for i in range(n):
    for j in range(n):
        cubo[j].append([0]*n)

print(cubo)

for x in range(n):
    for y in range(n):
        for z in range(n):
            mod = int(input("Ingrese el numero que quiere en esta celda: "))
            cubo[x][y][z] = mod
            print(cubo)

part_x = int(input("O o 1 para x"))
part_y = int(input("O o 1 para y"))
part_z = int(input("O o 1 para z"))

print(cubo[part_x][part_y][part_z])
