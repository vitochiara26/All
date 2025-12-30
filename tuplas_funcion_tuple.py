'''Funcion tuple() para generar tuplas'''
#Ejemplo 1 - Crear una coordenada con tuple()
print("***** Ejemplo #1 ***** \n")
x = 10
y = 5

print(f"Las coordenadas son: {x} & {y}")
coordenada = tuple([x, y])
print(f"La tupla es: {coordenada} \n")

#Ejemplo 2 - Convertir un string a tupla
print("***** Ejemplo #2 ***** \n")
texto = input("Introduce un String: ")
tupla_texto = tuple(texto)
print(f"La tupla es: {tupla_texto} \n ")

#Ejemplo 3 - Convertir una diccionario a tupla
print("***** Ejemplo #3 ***** \n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3
                }
print(numbers_dict, '\n')

tupla_numbers= tuple(numbers_dict)
print(f"La tupla es: {tupla_numbers} \n ")

#Ejemplo 4 - Convertir un diccionario a tupla (valores)
print("***** Ejemplo #4 ***** \n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3
                }
print(numbers_dict, '\n')

tupla_numbers= tuple(numbers_dict.values())
print(f"La tupla es: {tupla_numbers} \n ")

#Ejemplo 5 - Convertir un diccionario a tupla (clave:valor)
print("***** Ejemplo #5 ***** \n")
numbers_dict = {"uno": 1,
                "dos": 2,
                "tres": 3
                }
print(numbers_dict, '\n')

tupla_numbers= tuple(numbers_dict.items())
print(f"La tupla es: {tupla_numbers} \n ")