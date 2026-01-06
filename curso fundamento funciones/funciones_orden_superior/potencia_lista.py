def cuadrado(x):
    return x * x


def cubo(x):
    return x ** 3


def aplicar_funcion_a_lista(funcion, lista):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


lista_numeros = [1 , 2, 3, 4, 5]
resultados = aplicar_funcion_a_lista(cuadrado, lista_numeros)
print(resultados)
resultados = aplicar_funcion_a_lista(cubo, lista_numeros)
print(resultados)
