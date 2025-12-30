frase = input("Introduce una frase: ")
letra_break = input("Con que frase deseas terminar el bucle?: ")

for letra in frase :
    if letra.lower() == letra_break.lower() :
        print("Fin del programa, la sentencia 'break' se ha cumplido.")
        break
    elif letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u" :
        continue
    print(letra, end = "")


