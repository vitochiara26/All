'''solucion del profesor'''
import random

print("Bienvenido a 'Adivina el Numero Secreto'")
print("He seleccionado un numero entre 1 y 100. ¡Adivina cual es!")

numero_secreto = random.randint(1,100)
intentos_maximos = 10
adivinanza = 0

for intento in range(1, intentos_maximos + 1):
    print(f"\nIntento {intento}/{intentos_maximos}")

    try:
        adivinanza = int(input("Ingresa tu adivinanza: "))
        if adivinanza < numero_secreto:
            print("El numero es mayor.")
        elif adivinanza > numero_secreto:
            print("El numero es menor.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el numero secreto ({numero_secreto}) en {intento} intentos!")
            break
    except ValueError:
        print("Debes ingresar un numero entero.")
    except Exception:
        print(f"Debes ingresar un numero entero: {Exception}")

if adivinanza != numero_secreto:
    print(f"\nLo siento el numero secreto era {numero_secreto}. ¡Mejor suerte la proxima vez!")

input("\nPresiona 'ENTER' para salir")
