string = input("Introduce un string para invertirlo: ")
espacio1 = ""
espacio2 = ""
frase = ""

for letra in string :
    espacio1 = letra
    espacio1 += espacio2
    letra += espacio2
    frase = letra
    espacio2 = espacio1

print(frase)
