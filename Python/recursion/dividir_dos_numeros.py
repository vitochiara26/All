def dividir(dividendo, divisor):
    if divisor == 0:
        raise ZeroDivisionError('El divisor no puede ser 0')
    elif dividendo == divisor:
        return 1
    elif dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)

print('{}//{} = {}'.format(5, 2, dividir(5, 2)))
