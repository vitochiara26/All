def sum_numeros(*numeros):
    print(numeros)
    return sum(numeros)
    resultado = sum(numeros)
    print(resultado)


sum_numeros(1, 2, 3, 4, 5, 6, 7)
# *args