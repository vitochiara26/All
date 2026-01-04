'''Expresiones de comprension'''
#[expresion for element in iterable if condition]

#sin usar expresiones de comprension
sqrt_list = []
print(sqrt_list)
for number in range(10):
    sqrt = number ** 2
    sqrt_list.append(sqrt)
print(sqrt_list, '\n')

#Utilizando expresiones de comprension
sqrt_list_dos = []
print(sqrt_list_dos)
sqrt_list_dos.extend([number ** 2 for number in range(10)])
print(sqrt_list_dos, '\n')

sqrt_list_tres = []
print(sqrt_list_tres)
sqrt_list_tres.extend([number ** 2 for number in range(10) if number % 2 == 0])
print(sqrt_list_tres, '\n')

#Crear diccionario con expreciones de compresion
personas = [("Carlos", 30), ("Gerardo", 25), ("Maria", 35)]
dict_personas = {nombre: edad for nombre, edad in personas if edad >= 30}
print(dict_personas)
