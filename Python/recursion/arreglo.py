def mayor_elemento(array, n):
    if n == 1:
        return array[0]
    
    max_resto = mayor_elemento(array, n-1)

    return array[n-1] if array[n-1] > max_resto else max_resto

def sumar_elementos(array, n):
    if n == 0:
        return 0
    
    return array[n-1] + sumar_elementos(array, n-1)

def calcular_media(array, n):
    if n == 0: return 0
    
    return sumar_elementos(array, n-1) / n

def esta_ordenado(array, n):
    if n <= 1:
        return True
    
    if array[n-1] < array[n-2]:
        return False
    
    return esta_ordenado(array, n-1)

datos = [3, 7, 34, 12, 15, 20]
n = len(datos)

print(f"El elemento mayor en el arreglo es: {mayor_elemento(datos, n)}")
print(f"La suma de los elementos del arreglo es: {sumar_elementos(datos, n)}")
print(f"El promedio de los elementos del arreglo es: {calcular_media(datos, n)}")
print(f"El elemento esá ordenado: {esta_ordenado(datos, n)}")

