import os
from time import sleep

def imprimir_tablero_emojis(tablero, pos_actual):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- TOUR DEL CABALLO (Visualización) ---\n")
    
    for r in range(8):
        fila = []
        for c in range(8):
            if (r, c) == pos_actual:
                fila.append("🐎") # Posición actual del caballo
            elif tablero[r][c] != 0:
                # Si fue visitada, cambiamos color según la paridad original
                # Rojo claro si la suma de coordenadas es par (blanca), rojo oscuro si es impar (negra)
                fila.append("🟥" if (r + c) % 2 == 0 else "🟫")
            else:
                # Tablero original
                fila.append("⬜" if (r + c) % 2 == 0 else "⬛")
        print(" ".join(fila))
    print("\nCalculando siguiente salto...")

def obtener_movimientos_validos(tablero, pos):
    movs = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
    return [(pos[0]+m[0], pos[1]+m[1]) for m in movs 
            if 0 <= pos[0]+m[0] < 8 and 0 <= pos[1]+m[1] < 8 
            and tablero[pos[0]+m[0]][pos[1]+m[1]] == 0]

def tour_del_caballo(tablero, pos, contador, pausa):
    tablero[pos[0]][pos[1]] = contador
    imprimir_tablero_emojis(tablero, pos)
    sleep(pausa)
    
    if contador == 64:
        return True
    
    posibles = obtener_movimientos_validos(tablero, pos)
    posibles.sort(key=lambda p: len(obtener_movimientos_validos(tablero, p)))
    
    for sig_pos in posibles:
        if tour_del_caballo(tablero, sig_pos, contador + 1, pausa):
            return True
            
    tablero[pos[0]][pos[1]] = 0 # Backtracking
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
tour_del_caballo(tablero, (0, 0), 1, pausa)