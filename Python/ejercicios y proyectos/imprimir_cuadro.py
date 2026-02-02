n = int(input("Ingrese el tamaño del cuadrado: "))

for i in range(n):
    if i == 0:
        print("X "*n)
    elif i == n-1:
        print("X "*n)
    else :
        print("X "+("  "*(n-2))+"X ")
