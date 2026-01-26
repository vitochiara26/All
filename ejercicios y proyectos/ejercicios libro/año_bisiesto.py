"""Solicitar un valor entero que representa un año e indicar si se trata de un año bisiesto"""
try:
    año = int(input("Ingrese el año que desea saber si es bisiesto o no: "))
except ValueError:
    print("Ingrese numeros validos")
    exit()

if año % 4 == 0 :
    if año % 100 == 0 :
        if año % 400 == 0 :
            print(f"{año} es bisiesto")
        else :
            print(f"{año} no es bisiesto")
    else :
        print(f"{año} es bisiesto")
else :
    print(f"{año} no es bisiesto")
