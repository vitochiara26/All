def cuadrado(x):
    return x * x


def cubo(x):
    return x ** 3


def aplicar(funcion, valor):
        return funcion(valor)


resultado = aplicar(cuadrado, 5)
print(resultado)

resultado = aplicar(cubo, 3)
print(resultado)
