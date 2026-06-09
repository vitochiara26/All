def busqueda_binaria(array, e, inicio, fin):
    if inicio > fin:
        return False
    
    medio = (inicio + fin) // 2
    
    if array[medio] == e:
        return True
    
    elif e < array[medio]:
        return busqueda_binaria(array, e, inicio, medio-1)
    
    else:
        return busqueda_binaria(array, e, medio + 1, fin)

datos = [1, 3, 5, 7, 9, 11, 13, 15]
elemento_buscado = 15

print(f"El elemento '{elemento_buscado}' \
se encuentra en el arreglo?: {busqueda_binaria(datos, elemento_buscado, 0, len(datos)-1)}")