'''Adivina el numero'''
from random import randint
print("Bienvenido a 'Adivina el Numero Secreto'")
print("He seleccionado un numero entre 1 y 100. ¡Adivina cual!")

secret_number = randint(1, 100)
adivinado = False
attemps = 10
attemp = 1

while adivinado is False:
    if attemps == 0:
        print("No te quedan mas intentos.")
        print(f"El numero secreto era el {secret_number}")
        break
    while attemps > 0:
        try:
            adivinacion = int(input(f"Intento {attemp}/10\nIngresa tu adivinanza: "))
        except ValueError:
            print("Debes ingresar un numero entero")
            attemp += 1
            attemps -= 1
            continue

        if adivinacion == secret_number:
            if attemps in (10, 9):
                print("Haz adivinado, tienes muchisima suerte!")
                adivinado = True
                break
            if attemps in (8, 7):
                print("Haz adivinado, tienes mucha suerte!")
                adivinado = True
                break
            if attemps in (6, 5):
                print("Haz adivinado, que suerte!")
                adivinado = True
                break
            if attemps in (4, 3):
                print("Haz adivinado, poca suerte te queda.")
                adivinado = True
                break
            if attemps in (2, 1):
                print("Haz adivinado, por poco no lo logras.")
                adivinado = True
                break
        if adivinacion < secret_number:
            print("El numero seleccionado es mayor a tu adivinanza")
        if adivinacion > secret_number:
            print("El numero seleccionado es menor a tu adivinanza")

        if adivinado is False:
            attemps -= 1
            attemp += 1
            if attemps > 0:
                print(f"Haz fallado, intentos restantes: {attemps}.\n")
            if attemps == 0:
                print("Haz fallado, mejor suerte para la proxima.")

