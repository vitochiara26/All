'''Tuplas'''
tupla_vacia = ()
print(f"Tupla vacia: {tupla_vacia}")
print(f"El tipo de dato de esta tupla es: {type(tupla_vacia)} \n")

tupla_homogenea = (3, 2)
print(f"Tupla homogenea: {tupla_homogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_homogenea)} \n")

tupla_heterogenea = (3, True, "Hola", 2.5)
print(f"Tupla heterogenea: {tupla_heterogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea)} \n")

tupla_heterogenea_dos = ([1, 2, 3], {"uno": 1, "dos": 2}, (3,2))
print(f"Tupla heterogenea: {tupla_heterogenea_dos}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea_dos)} \n")

tupla_un_elemento = (3, )
print(f"Tupla de un elemento: {tupla_un_elemento}")
print(f"El tipo de dato de esta tupla es: {type(tupla_un_elemento)} \n")

tupla_sin_parentesis = 3, True, "Hola", 2.5
print(f"Tupla sin parentesis: {tupla_sin_parentesis}")
print(f"El tipo de dato de esta tupla es: {type(tupla_sin_parentesis)} \n")
