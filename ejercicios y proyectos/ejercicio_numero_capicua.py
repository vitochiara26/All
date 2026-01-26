'''Algoritmo para determinar si un numero es capicua o no'''

num = int(input("Ingrese un número entero de cinco digitos: "))
NUM_VALIDO = False
if 10000 <= int(num) <= 99999:
    NUM_VALIDO = True
else :
    print("Ingrese un numero de 5 digitos")

#43521
if NUM_VALIDO is True:
    valor1 = num // 10000
    valor2 = (num % 10000) // 1000
    valor4 = (num % 100) // 10
    valor5 = num % 10

    if valor1 == valor5 and valor2 == valor4:
        print(f"El numero {num} es capicua")
    else :
        print(f"El numero {num} NO es capicua")
