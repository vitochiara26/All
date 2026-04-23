matriz_alfabeto =[
    ['A', 'B', 'C', 'D', 'E'],
    ['F','G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'X', 'Y', 'Z']
]

mensaje = 'hellomundo'
tammaño_mensaje = len(mensaje)

posiciones_mensaje = [
    ['']*tammaño_mensaje,
    ['']*tammaño_mensaje
]

posiciones_volteadas = [
    ['']*tammaño_mensaje,
    ['']*tammaño_mensaje
]

#entrega las posiciones de cada letra del mensaje
for letra in range(tammaño_mensaje):
    found = False
    for fila in range(5):
        for columna in range(5):
            if mensaje[letra].upper() == matriz_alfabeto[fila][columna]:
                found = True
                posiciones_mensaje[0][letra] = fila 
                posiciones_mensaje[1][letra] = columna
            if found:
                break
        if found:
            break
        

#encripta mensaje
pos_vol = 0
indice = 0
for pos in range(tammaño_mensaje):
    if tammaño_mensaje % 2 != 0:
        if pos <= tammaño_mensaje//2:
            try: 
                posiciones_volteadas[0][pos_vol] = posiciones_mensaje[0][indice]
                posiciones_volteadas[0][pos_vol+1] = posiciones_mensaje[1][indice]
                indice +=1
                pos_vol += 2
            except Exception:
                posiciones_volteadas[1][0] = posiciones_mensaje[0][indice]
                indice +=1
                pos_vol = 1
        else :
            posiciones_volteadas[1][pos_vol] = posiciones_mensaje[0][indice]
            posiciones_volteadas[1][pos_vol+1] = posiciones_mensaje[1][indice]
            indice +=1
            pos_vol += 2
    else :
        if pos < tammaño_mensaje//2:
            posiciones_volteadas[0][pos_vol] = posiciones_mensaje[0][indice]
            posiciones_volteadas[0][pos_vol+1] = posiciones_mensaje[1][indice]
            indice +=1
            pos_vol += 2
        else :
            try:
                posiciones_volteadas[1][pos_vol] = posiciones_mensaje[0][indice]
                posiciones_volteadas[1][pos_vol+1] = posiciones_mensaje[1][indice]
                indice +=1
                pos_vol += 2
            except Exception:
                pos_vol = 0
                posiciones_volteadas[1][pos_vol] = posiciones_mensaje[0][indice]
                posiciones_volteadas[1][pos_vol+1] = posiciones_mensaje[1][indice]
                indice +=1
                pos_vol += 2


#desencripta mensaje
# pos_ini = 0
# for pos in range(tammaño_mensaje):
#     if tammaño_mensaje % 2 != 0:
#         if pos <= tammaño_mensaje//2:
#             try:
#                 posiciones_volteadas[0][pos] = posiciones_mensaje[0][pos_ini]
#                 posiciones_volteadas[1][pos] = posiciones_mensaje[0][pos_ini+1]
#                 pos_ini += 2
#             except Exception:
#                 pos_ini = 0
#                 posiciones_volteadas[1][pos] = posiciones_mensaje[1][pos_ini]
#                 pos_ini += 1
#         else:
#             posiciones_volteadas[0][pos] = posiciones_mensaje[1][pos_ini]
#             posiciones_volteadas[1][pos] = posiciones_mensaje[1][pos_ini+1]
#             pos_ini += 2
#     else :
#         if pos < tammaño_mensaje//2:
#             posiciones_volteadas[0][pos] = posiciones_mensaje[0][pos_ini]
#             posiciones_volteadas[1][pos] = posiciones_mensaje[0][pos_ini+1]
#             pos_ini += 2
#         else:
#             try:
#                 posiciones_volteadas[0][pos] = posiciones_mensaje[1][pos_ini]
#                 posiciones_volteadas[1][pos] = posiciones_mensaje[1][pos_ini+1]
#                 pos_ini += 2
#             except Exception:
#                 pos_ini = 0
#                 posiciones_volteadas[0][pos] = posiciones_mensaje[1][pos_ini]
#                 posiciones_volteadas[1][pos] = posiciones_mensaje[1][pos_ini+1]
#                 pos_ini += 2



indice = 0 
mensaje_interpr = ''
while indice < tammaño_mensaje:
    mensaje_interpr += matriz_alfabeto[posiciones_mensaje[0][indice]][posiciones_mensaje[1][indice]]
    indice += 1
print(mensaje_interpr)
print(posiciones_mensaje[0], "\n", posiciones_mensaje[1],'\n', sep='')


#intepretar posiciones y crear mensaje
indice = 0 
mensaje_interpr = ''
while indice < tammaño_mensaje:
    mensaje_interpr += matriz_alfabeto[posiciones_volteadas[0][indice]][posiciones_volteadas[1][indice]]
    indice += 1

print(mensaje_interpr)
print(posiciones_volteadas[0], "\n", posiciones_volteadas[1], sep='')
