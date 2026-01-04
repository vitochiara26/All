'''Seleccionador de Nombres'''
#Mi solucion
names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")
print(f"Tupla original: {names_tuple}")

valid_selection = False
while valid_selection is False:
    selection = int(input("Introduce un numero entero entre 1 y 5: "))

    if 0 <= (selection - 1) <= 4:
        print(f"El nombre es: {names_tuple[selection-1]}.\n")
        valid_selection = True
    else:
        print("Opcion no disponible, intente de nuevo.\n")


#Solucion del profesor
names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")
print(f"Tupla original: {names_tuple}")

validator = 0
while validator == 0:
    number = int(input("Introduce un numero entero entre 0 y 4: "))

    if 0 <= number <= 4:
        print(f"El nombre es: {names_tuple[number]}.")
        validator = 1
    else:
        print("Error!!!: Numero invalido, vuelve a intentar.\n")
