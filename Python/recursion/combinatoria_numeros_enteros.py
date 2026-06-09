def combinatoria(n, k):
    #si k == 0 solo hay una forma de elegir 0 elementos, resultado es 1
    #si k == n solo hay una forma de elegir todos los elementos, resultado es 1
    if k == 0 or k == n:
        return 1
    
    if k > n:
        return 0
        
    #n-1, k-1 
    #ahora necesito escojer k-1 objeto/s de los n-1 objeto/s restantes
    #y sumarla a la exclusion de escojer k objetos de las n-1 objetos restantes 
    return combinatoria(n - 1, k - 1) + combinatoria(n - 1, k)

#De cuántas formas puedo elegir 2 objetos de un grupo de 4 objetos 
resultado = combinatoria(4, 2)
print(f"El valor de la combinatoria es: {resultado}")