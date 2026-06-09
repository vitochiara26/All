def explorar_combinacionaciones(index, datos_objetos, mochila, combinaciones):
    if index == 4:
        registro_mochila = []
        for objeto in mochila:
            registro_mochila.append(objeto)
        combinaciones.append(registro_mochila)
        return

    nombre_objeto = datos_objetos[0][index]
    peso_objeto = datos_objetos[1][index]
    valor_objeto = datos_objetos[2][index]
    mochila.append([nombre_objeto, peso_objeto, valor_objeto])
    explorar_combinacionaciones(index + 1, datos_objetos, mochila, combinaciones)
    
    mochila.pop()
    explorar_combinacionaciones(index + 1, datos_objetos, mochila, combinaciones)

def revisar_relacion_mochila(combinaciones, capacidad_maxima):
    mejor_mochila = []
    peso_mochila = 0
    mejor_valor = 0
    
    for combinacion in combinaciones:
        peso_total = 0
        valor_total = 0
        
        for objeto in combinacion:
            peso_total += objeto[1]
            valor_total += objeto[2]
        
        if peso_total <= capacidad_maxima:
            if valor_total > mejor_valor:
                mejor_valor = valor_total
                mejor_mochila = combinacion
                peso_mochila = peso_total

    return mejor_mochila, peso_mochila, mejor_valor


datos_objetos = [ ['A','B','C','D','E','F','G','H'],
            [6, 10, 3, 2, 5, 1, 9, 7],
            [15, 5, 6, 4, 10, 8, 4, 7]
            ]

datos_objetos_prueba = [ ['A','B','C','D'],
            [6, 10, 3, 2],
            [15, 5, 6, 4]
            ]

mochila = []
capacidad_maxima = 10
combinaciones = []

explorar_combinacionaciones(0, datos_objetos_prueba, mochila, combinaciones)
mejor_mochila, peso_mochila, mejor_valor = revisar_relacion_mochila(combinaciones, capacidad_maxima)

print(
    f"La mejor mochila es {mejor_mochila},\n\
su peso es de {peso_mochila}kg y su valor total es de {mejor_valor}$")
