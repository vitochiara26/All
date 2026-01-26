"""Dada una letra cualquiera indicar si es consonante, vocal o un dígito"""
letra = input("Ingesa cualquier caracter, letra o numero: ").lower()

if len(letra) > 1 :
    print("Ingrese solo un caracter, no mas, ya sea letra o numero")
    exit(0)

if letra in '0123456789':
    print(f"El caracter '{letra}' es un numero")

elif letra in 'aeiou' :
    print(f"El caracter '{letra}' es una vocal")

else :
    print(f"El caracter '{letra}' es una consonante")
