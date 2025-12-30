print("Conversor.\n")

print("Opciones:\n")

print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero.\n")

selector = int(input("Cual es tu opcion?: "))

if selector == 1 :
    print("Conversor de numero a palabra.\n")
    
    numero = int(input("Cual es el numero que deseas convertir a palabra?: "))
    
    if numero == 1 :
        print("La palabra es 'UNO'.")
    elif numero == 2 :
        print("La palabra es 'DOS'.")
    elif numero == 3 :
        print("La palabra es 'TRES'.")
    elif numero == 4 :
        print("La palabra es 'CUATRO'.")
    elif numero == 5 :
        print("La palabra es 'CINCO'.")
    else :
        print("el numero seleccionado no esta registrado.")
        
elif selector == 2 :
    print("Conversor de palabra a numero.\n")
    
    palabra = input("Cual es la palabra que deseas convertir a numero?: ")
    palabra = palabra.lower()
    
    if palabra == "uno" :
        print("El numero es '1'.")
    elif palabra == "dos":
        print("El numero es '2'.")
    elif palabra == "tres":
        print("El numero es '3'.")
    elif palabra == "cuatro":
        print("El numero es '4'.")
    elif palabra == "cinco":
        print("El numero es '5'.")
    else :
        print("la palabra seleccionada no esta registrada.")

else :
    print("Opcion incorrecta.")

print("Fin.")
