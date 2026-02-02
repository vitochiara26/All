N = int(input("Ingrese el tamaño N (impar): "))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        
        # Comprobamos si estamos en la diagonal principal O en la secundaria
        # (Usamos 'or' porque queremos que se 
        # pinte si cumple CUALQUIERA de las dos)
        if i == j or (i + j == N + 1):
            print("X", end=" ")
        else:
            print(".", end=" ") 
            # Usamos un punto para que el vacío se vea ordenado
            
    print() # Salto de línea