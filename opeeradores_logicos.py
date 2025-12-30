#conjuncion
print("Conjuncion (and)")

num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5 :
    print("El numero", num_uno , "cumple con la condicion.\n")
else :
    print("El numero", num_uno , "NO cumple con la condicion.\n")

#disyuncion
print("Disyuncion (or)")

palabra = input("Para cumplir con la condicion escribe 'si' o 'yes': ")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes" :
    print("La condicion se ha cumplido.\n")
else :
    print("La condicion NO se ha cumplido.\n")

#negacion
print("Negacion (not)")

num_uno = int(input("Introduce un numero igual a 5: "))

if not num_uno == 5 :
    print("El numero es diferente de cinco y SI cumple la condicion.\n")
else :
    print("El numero es igual a cinco y NO se cumple la condicion.\n")
