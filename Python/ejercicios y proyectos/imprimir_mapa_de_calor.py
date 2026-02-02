N = int(input("Ingrese el tamaño N (impar): "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 1. Calculamos las 4 distancias
        d_arriba = i
        d_izquierda = j
        d_abajo = N - i + 1
        d_derecha = N - j + 1
        
        # 2. Buscamos el mínimo de forma manual
        capa = d_arriba
        if d_izquierda < capa:
            capa = d_izquierda
        if d_abajo < capa:
            capa = d_abajo
        if d_derecha < capa:
            capa = d_derecha
        
        # 3. Imprimimos el número seguido de un espacio para que se vea ordenado
        print(capa, end=" ")
        
    # Salto de línea después de cada fila
    print()