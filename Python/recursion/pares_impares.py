def es_par(n):
    if n == 0: 
        return True
    else :
        return es_impar(n - 1)

def es_impar(n):
    if n == 0:
        return False
    else:
        return es_par(n - 1)


numero = 7
print(f"El numero {numero} es par: {es_par(numero)}")
print(f"El numero {numero} es impar: {es_impar(numero)}")
