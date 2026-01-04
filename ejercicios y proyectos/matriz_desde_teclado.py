filas = int(input("Cuantas filas tendra la matriz?: "))
columnas = int(input("Cuantas columnas tendra la matriz?: "))

matrix = []

for indice_fila in range(filas) :
    lista_fila = []
    for indice_columna in range(columnas) :
        lista_fila.append(int(input(f"Introduce un elemento para la fila {indice_fila}: ")))
    matrix.append(lista_fila)

for indice_fila in matrix :
    print(indice_fila)