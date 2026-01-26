"""Ejercicio"""
num = int(input("Ingrese un numero de 4 digitos: "))

if 999 < num > 9999 :
    print("Ingrese un numero mayor a 999 y menor a 9999")
    exit(0)

digito_uno = num // 1000
digito_dos = (num % 1000) // 100
digito_tres = (num % 100) // 10
digito_cuatro = num % 10

digitos_uno_dos = digito_uno * 10 + digito_dos
digitos_tres_cuatro = digito_tres * 10 + digito_cuatro

if digitos_uno_dos > digitos_tres_cuatro :
    print(f"{num} es un numero feliz")
else :
    print(f"{num} no es un numero feliz")

if digito_uno < digito_dos < digito_tres < digito_cuatro :
    print(f"{num} es un numero creciente")
else :
    print(f"{num} no es un numero creciente")

if digitos_uno_dos > digitos_tres_cuatro and digito_uno < digito_dos < digito_tres < digito_cuatro :
    print(f"{num} es un numero muy feliz")

if digitos_uno_dos < digitos_tres_cuatro and not digito_uno < digito_dos < digito_tres < digito_cuatro :
    print(f"{num} es un numero infeliz")
