def mezclar(izq, der):
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def ordenamiento_estricto(array):
    n = len(array)
    
    if n == 2 :
        
        if array[0] > array[1]:
            
            array[0], array[1] = array[1], array[0]
            
        return array
    
    if n < 2:
        return array
    
    mitad = n // 2
    parte_izquierda = ordenamiento_estricto(array[:mitad])
    parte_derecha = ordenamiento_estricto(array[mitad:])
    
    return mezclar(parte_izquierda, parte_derecha)

datos_uno = [38, 27, 43, 3]
print(f"Original: {datos_uno} | Ordenado: {ordenamiento_estricto(datos_uno)}")

datos_dos = [12, 11, 13, 5, 6]
print(f"Original: {datos_dos} | Ordenado: {ordenamiento_estricto(datos_dos)}")

datos_tres = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print(f"Original: {datos_tres} | Ordenado: {ordenamiento_estricto(datos_tres)}")
