def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    :param n: (int) Número entero no negativo.
    :return: (int) El factorial de n.
    :raises RecursionError: Si n es un número negativo.
    """
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n - 1)


resultado_factorial = factorial(5)
print(resultado_factorial)

#help(factorial)
print(factorial.__doc__)