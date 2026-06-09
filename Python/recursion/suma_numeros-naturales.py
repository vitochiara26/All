def sumar_numeros(n, index = 1):
    if index >= n:
        return n
    
    return index + sumar_numeros(n, index + 1)

print(sumar_numeros(10))