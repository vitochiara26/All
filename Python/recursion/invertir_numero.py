def invertir_numero(n):
    def recursiva(n, invertido):
        if n == 0:
            return invertido

        return recursiva(n//10, (invertido * 10) + (n % 10))
    
    return recursiva(n, 0)

numero = 653
numero_invertido = invertir_numero(numero)
print(f"Numero original: {numero} | Numero invertido: {numero_invertido}")
