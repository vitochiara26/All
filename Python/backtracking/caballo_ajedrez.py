from time import sleep 


def encontrar_caballo(tablero):
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna]  == '  1':
                return [fila, columna]
            

def verificar_tablero(tablero):
    for fila in range(8):
        for columna in range(8):
            if tablero[fila][columna]  == '  0':
                return False
    return True

def movilizar_caballo(pos_caballo, tablero, movs_caballo, contador = 2):
    for mov in movs_caballo:
        salto_caballo = [pos_caballo[0] + mov[0], pos_caballo[1] + mov[1]]
        if ((-1 < salto_caballo[0] < 8) and (-1 < salto_caballo[1] < 8)) and tablero[salto_caballo[0]][salto_caballo[1]] == '  0':
            if contador < 10:
                tablero[salto_caballo[0]][salto_caballo[1]] = '  ' + str(contador)
                print(mostrar_tablero(tablero))
                sleep(pausa)
                movilizar_caballo(salto_caballo, tablero, movs_caballo, contador + 1)
                tablero_lleno = verificar_tablero(tablero)
                if tablero_lleno:
                    return tablero
                else:
                    tablero[salto_caballo[0]][salto_caballo[1]] = '  0'
                    print(f"eliminamos el movimiento {contador}")
                    print(mostrar_tablero(tablero))
                    sleep(pausa)
            else: 
                tablero[salto_caballo[0]][salto_caballo[1]] = ' ' + str(contador)
                print(mostrar_tablero(tablero))
                sleep(pausa)
                movilizar_caballo(salto_caballo, tablero, movs_caballo, contador + 1)
                tablero_lleno = verificar_tablero(tablero)
                if tablero_lleno:
                    return tablero
                else:
                    tablero[salto_caballo[0]][salto_caballo[1]] = '  0'
                    print(f"eliminamos el movimiento {contador}")
                    print(mostrar_tablero(tablero))
                    sleep(pausa)

def mostrar_tablero(tablero):
    tablero_terminal = ''
    for fila in range(8):
        for columna in range(8):
            tablero_terminal+= tablero[fila][columna]
        tablero_terminal += '\n'
    return tablero_terminal


tablero =  [
            ['  0','  0','  0','  0','  0','  0','  0','  1'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0']
        ]
def mostrar_tablero(tablero):
    tablero_terminal = ''
    for fila in range(8):
        for columna in range(8):
            tablero_terminal+= tablero[fila][columna]
        tablero_terminal += '\n'
    return tablero_terminal


tablero =  [
            ['  0','  0','  0','  0','  0','  0','  0','  1'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0'],
            ['  0','  0','  0','  0','  0','  0','  0','  0']
        ]

pausa = 0.1
movs_caballo = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
pos_caballo = encontrar_caballo(tablero)

pausa = 0.1
movs_caballo = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
pos_caballo = encontrar_caballo(tablero)
movilizar_caballo(pos_caballo, tablero, movs_caballo)