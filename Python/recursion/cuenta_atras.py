def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print('Holaaa!')
    print(f'Orden de liberacion {numero}')

cuenta_atras(6)

def calcular_factorial(numero):
    if numero > 1: numero *= calcular_factorial(numero - 1)
    return numero

print(calcular_factorial(5))
