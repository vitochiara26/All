bosque = []

while True:
    try:
        limite_i = int(input("Ingrese un numero entero menor a 100 para definir el ancho del bosque: "))
        limite_j = int(input("Ingrese otro numero entero menor a 100 para definir lo largo del bosque: "))
    except Exception:
        print("Debe ingresar solo valores numericos.")
        continue
    if isinstance(limite_i, int) and isinstance(limite_j, int):
        if 0 < limite_i < 100 and 0 < limite_j < 100:
            break
        else :
            print("Debe ingresar un numero entero mayor a 0 y menor a 100")

for fila in range(0,limite_i):
    fila_temp = []
    for columna in range(0, limite_j):
        fila_temp.append(4)
    
