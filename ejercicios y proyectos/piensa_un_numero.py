'''Proyecto 2 - Piensa en un numero'''
import random as ra
print("Piensa en un numero entre 1 y 100. Yo trataré de adivinarlo.")
menor = 1
mayor = 100
correcto = False
intento = 0

try:
    while correcto is False:
        intento += 1
        adivinando = ra.randint(menor, mayor)

        print(f"¿Es {adivinando} tu numero?")
        pista = input("Ingresa 'mayor', 'menor' o 'correcto': ").lower()

        if not pista in ('mayor', 'menor', 'correcto'):
            print("Respuesta no válida")
        elif pista == 'mayor':
            menor = adivinando + 1
        elif pista == 'menor':
            mayor = adivinando - 1
        else:
            print(f"¡Adivine tu numero ({adivinando}) en {intento} intentos")
            correcto = True
except Exception as e:
    print(e)
