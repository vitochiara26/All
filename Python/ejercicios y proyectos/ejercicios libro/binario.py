entrada = input("Ingrese un caracter numerico 0 o 1: ")
entrada_acumulada = ""
numero_decimal = 0
while entrada != "-1":
    if int(entrada) > 1:
        print("Ingrese solo un caracter numerico 0 o 1")
        print("Ingrese '-1' para finalizar o...")
        entrada = input("ingrese otro caracter numerico 0 o 1: ")
        continue
    entrada_acumulada = entrada + entrada_acumulada
    print("Ingrese '-1' para finalizar o...")
    entrada = input("ingrese otro caracter numerico 0 o 1: ")

posicion = 0
for n in entrada_acumulada:
    if n == "1":
        numero_decimal += 2**posicion
    posicion += 1 

print(numero_decimal)