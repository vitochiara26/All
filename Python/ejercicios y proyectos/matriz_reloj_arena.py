import time as t
n = 10
matrix = []
for i in range(n):
    matrix.append(['  ']*n)


for i in range(n):
    for j in range(n):
            pass
#primera impresion
for x in range(n):
    for y in range(n):
        if x == 0:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        else :
            print(matrix[x][y], end=" ")
    print()
input("Presione 'Enter' para continuar")
#segunda impresion
a = 1
b = 2
for x in range(n):
    for y in range(n):
        if x == 0 :
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        elif x == a and y == n-b:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
            a += 1
            b += 1
        else :
            print(matrix[x][y], end=" ")
    print()
input("Presione 'Enter' para continuar")
#Tercera impresion
a = 1
b = 2
for x in range(n):
    for y in range(n):
        if x == 0 :
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        elif x == a and y == n-b:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
            a += 1
            b += 1
        elif x == n-1:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        else :
            print(matrix[x][y], end=" ")
    print()
input("Presione 'Enter' para continuar") 

a = 1
b = 2
for x in range(n):
    for y in range(n):
        if x == 0 :
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        elif x == a and y == n-b:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
            a += 1
            b += 1
        elif x == n-1:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        elif x == y:
            matrix[x][y] = "X "
            print(matrix[x][y], end=" ")
        else :
            print(matrix[x][y], end=" ")
    print()
input("Presione 'Enter' para ver animación")
fotograma = 0
while True: 
    if fotograma == 0:
        fotograma = 1
        a = 1
        b = 2
        for x in range(n):
            for y in range(n):
                if x == 0 :
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                elif x == a and y == n-b:
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                    a += 1
                    b += 1
                elif x == n-1:
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                elif x == y:
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                elif y == 0 or y == n-1  :
                    matrix[x][y] = "  "
                    print(matrix[x][y], end=" ")
                else :
                    print(matrix[x][y], end=" ")
            print()
        print()
        t.sleep(0.4)
    else: 
        fotograma = 0
        a = 1
        b = 2
        for x in range(n):
            for y in range(n):
                if (x == 0 and y > 0) and (x == 0 and y < n-1):
                    matrix[x][y] = "  "
                    print(matrix[x][y], end=" ")
                elif y == 0 or y == n-1 :
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                elif x == a and y == n-b:
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                    a += 1
                    b += 1
                elif x == y:
                    matrix[x][y] = "X "
                    print(matrix[x][y], end=" ")
                elif x == n-1:
                    matrix[x][y] = "  "
                    print(matrix[x][y], end=" ")
                else :
                    print(matrix[x][y], end=" ")
            print()
        print()
        t.sleep(0.4)

