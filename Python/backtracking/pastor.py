def es_seguro(estado):
    '''Esta funcion se pregunta si es seguro realizar in determinado
    moviento, teniendo establecidos cuales son los casos de peligro'''
    P, L, O, C = estado
    #se pregunta si el estado(la orilla donde este) del lobo es igual a la de la oveja
    #y si el el estado del pastor es distinto al del pastor
    if L == O and P != L:
        return False
    #igual se pregunta si la oveja se queda sola con la lechuga
    if O == C and P != O:
        return False
    #es seguro para cualquiera de los otros casos
    return True

def resolver(estado, historial):
    #si todos son 1 significa que ya todos cruzaron al otro lado del rio 
    if estado == (1,1,1,1):
        return historial
    
    P, L, O, C = estado
    #movimientos posibles del pastor, hacerlo solo o acompañado
    posibles = [
        (1-P, L, O, C),
        (1-P, 1-L, O, C),
        (1-P, L, 1-O, C),
        (1-P, L, O, 1-C),
    ]
    
    for siguiente in posibles:
        if es_seguro(siguiente) and siguiente not in historial:
            resultado = resolver(siguiente, historial + [siguiente])
            if resultado:
                return resultado
    return None


inicio = (0,0,0,0)
solucion = resolver(inicio, [inicio])

nombres = ["Pastor", "Lobo", "Oveja", "Lechuga"]

print("--- Inicio del Cruce ---")
for i, estado in enumerate(solucion):
    orilla_a = [nombres[j] for j in range(4) if estado[j] == 0]
    orilla_b = [nombres[j] for j in range(4) if estado[j] == 1]
    print(f"Paso {i}: Orilla A: {orilla_a} | Orilla B: {orilla_b}")