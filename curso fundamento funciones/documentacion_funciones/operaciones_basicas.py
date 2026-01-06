def operacion_basica(a, b):
    """
    Realiza operaciones básicas entre dos números.

    :param a:  (int o float) Primer número.
    :param b:  (int o float) Segundo número.
    :return:  Una tupla con los resultados de las operaciones.
                  - suma (int o float): Suma de a y b.
                  - resta (int o float): Resta de a y b.
                  - multiplicación (int o float): Producto de a y b.
                  - división (float): Cociente de a dividido por b. (si b no es cero)
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division


resultados = operacion_basica(8, 4)
print(resultados)

#help(operacion_basica)
print(operacion_basica.__doc__)