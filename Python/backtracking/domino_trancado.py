#def generar_fichas():
    #generar las 28 fichas del juego, desde 0;0 hasta 6;
#    return [(i,j) for i in range(7) for j in range(i, 7)]

def obtener_fichas_con(x, fichas_juego):
    #Devuelve el conjunto de las 7 fichas que contienen el numero x
    return {ficha for ficha in fichas_juego if x in ficha}

def buscar_tranques(fichas_juego):
    fichas_totales = fichas_juego
    
    #iteramos sobre cada posible numero de tranque (del 0 al 6)
    for x in range(7):
        fichas_criticas = obtener_fichas_con(x, fichas_totales)
        
        #se inicia el backtracking con este numero x
        #se coloca cualquiera de las piezas criticas como base
        for ficha in fichas_criticas:
            restantes = set(fichas_totales) - {ficha}
            
            #la punta izquierda (el inicio) de la mesa debe empezar con x 
            if ficha[0] == x:
                ficha_inicial = ficha
            else:
                ficha_inicial = (ficha[1], ficha[0]) 
            
            
            #se inicia el backtrack como generador con el contador en 1 porque es la primera ficha
            yield from backtrack_mesa([ficha_inicial], restantes, x, 1)

def backtrack_mesa(mesa, disponibles, x, criticas_usadas):
    punta_izq = mesa[0][0]
    punta_der = mesa[-1][1]
    
    #Tranque: si las puntas son x y todas las criticas estan en la mesa 
    if punta_izq == x and punta_der == x and criticas_usadas == 7:
        yield list(mesa)
        return

    #PODA: si ya no hay fichas criticas en el monton y ya no estamos en 'x' no se puede trancar
    if criticas_usadas < 7 and punta_der != x:
        #queda algun x disponible?
        if not any(x in f for f in disponibles):
            return
    
        
    #Intentamos colocar una ficha en la punta derecha
    for ficha in list(disponibles):
        if punta_der in ficha:
            nueva_ficha = ficha if ficha[0] == punta_der else (ficha[1], ficha[0])
            
            es_critica = x in ficha
            
            disponibles.remove(ficha) 
            mesa.append(nueva_ficha)
            
            yield from backtrack_mesa(mesa, disponibles, 
                                    x, criticas_usadas + (1 if es_critica else 0))
            
            #se deshace lo anterior para explorar otra ficha
            mesa.pop()
            disponibles.add(ficha)

fichas_juego = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                (3, 3), (3, 4), (3, 5), (3, 6),
                (4, 4), (4, 5), (4, 6),
                (5, 5), (5, 6),
                (6, 6)]

# Al ser un generador imprimimos los resultados uno a uno
contador = 0

print("Buscando tranques (los resultados se imprimirán en tiempo real)...")
for forma in buscar_tranques(fichas_juego):
    contador += 1
    if contador <= 5:  # Mostramos solo los primeros 5 ejemplos para no saturar la pantalla
        print(f"Tranque #{contador}: {forma}")
    
    if contador % 10000 == 0:
        print(f"... Procesados {contador} tranques legítimos hasta ahora ...")

print(f"\n¡Proceso completado! Se encontraron un total de {contador} formas de trancar el juego.")
