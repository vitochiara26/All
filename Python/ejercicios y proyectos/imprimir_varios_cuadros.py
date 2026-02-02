N = int(input("Ingrese el tamaño N (impar): "))

# 1. Bucle de filas empezando en 1
for i in range(1, N + 1):
    
    # 2. Bucle de columnas empezando en 1
    for j in range(1, N + 1):
        
        # --- CÁLCULO DE DISTANCIAS ---
        dist_arriba = i
        dist_izquierda = j
        dist_abajo = N - i + 1
        dist_derecha = N - j + 1
        
        # --- ENCONTRAR LA CAPA (Mínima distancia) ---
        capa = dist_arriba
        if dist_izquierda < capa:
            capa = dist_izquierda
        if dist_abajo < capa:
            capa = dist_abajo
        if dist_derecha < capa:
            capa = dist_derecha
            
        # --- REGLA DE DIBUJO ---
        # Ahora la Capa 1 (exterior) es IMPAR.
        # Por lo tanto: IMPAR = 'X', PAR = ' '
        if capa % 2 != 0:
            print("X ", end="")
        else:
            print("  ", end="")
            
    print() # Salto de línea al terminar cada fila