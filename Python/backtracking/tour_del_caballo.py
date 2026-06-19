import os
from time import sleep

def limpiar_pantalla():
    # 'cls' para Windows, 'clear' para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_tablero(tablero):
    limpiar_pantalla()
    print("Travesia del caballo por el tablero")
    print("-" * 23)
    for fila in tablero:
        # El formato {:>2} asegura que cada número ocupe 2 espacios, alineados a la derecha
        print(" ".join(f"{num:>2}" for num in fila))
    print("-" * 23)

def obtener_movimientos_validos(tablero, pos):
    movs = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
    return [(pos[0]+m[0], pos[1]+m[1]) for m in movs 
            if 0 <= pos[0]+m[0] < 8 and 0 <= pos[1]+m[1] < 8 
            and tablero[pos[0]+m[0]][pos[1]+m[1]] == 0]

def contar_grados(tablero, pos):
    return len(obtener_movimientos_validos(tablero, pos))

def tour_del_caballo(tablero, pos, contador, pausa):
    tablero[pos[0]][pos[1]] = contador
    
    imprimir_tablero(tablero)
    sleep(pausa)
    
    
    if contador == 64:
        return True
    
    posibles = obtener_movimientos_validos(tablero, pos)
    # Heurística: elegir la casilla con menos salidas futuras
    posibles.sort(key=lambda p: contar_grados(tablero, p))
    
    for sig_pos in posibles:
        if tour_del_caballo(tablero, sig_pos, contador + 1, pausa):
            return True
            
    # Backtracking
    tablero[pos[0]][pos[1]] = 0
    imprimir_tablero(tablero)
    sleep(pausa)
    return False

# Ejecución
tablero =  [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
pausa = 0.4

if tour_del_caballo(tablero, (5, 6), 1, pausa):
    imprimir_tablero(tablero)
else:
    print("No se encontró solución.")