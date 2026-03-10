try:
    frase = input("Ingrese una frase o palabra: ")
except Exception as e:
    raise "Algo hiciste mal" + e

tamaño_frase = len(frase)

i = 0 
j = -1

palindromo = True

while i < tamaño_frase // 2 :
    if frase[i] == frase[j]:
        i += 1
        j -= 1
        continue
    else :
        palindromo = False
        break
    

match palindromo:
    case True:
        print(f"La frase ingresada {frase} es un palindromo")
    case False:
        print(f"La frase ingresada {frase} no es un palindromo")
