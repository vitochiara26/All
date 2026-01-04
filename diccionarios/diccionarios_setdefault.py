'''El metodo setdefault() para asignar valores a claves de diccionarios'''
dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }
print(dict_name)
dict_name.setdefault("a", 4)
print(dict_name)

dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }
print(dict_name)
dict_name.setdefault("z")
print(dict_name)

dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }
print(dict_name)
dict_name.setdefault("z", 4)
print(dict_name)

fruits = {"manzana": 2,
          "banana": 3,
          "naranja": 1
          }
print(f"\n{fruits}\n")

#Intentamos agregar una clave que ya existe en el diccionario
return_value = fruits.setdefault("banana", 4)
print(f"El valor retornado de ('banana', 4) es: {return_value}")
print(f"El diccionario actualizado es: {fruits}\n")

#Intentamos agregar una clave que no existe en el diccionario sin valor
return_value = fruits.setdefault("kiwi")
print(f"El valor retornado de ('kiwi') es: {return_value}")
print(f"El diccionario actualizado es: {fruits}\n")

#Intentamos agregar una clave que no existe en el diccionario con valor
return_value = fruits.setdefault("mango", 5)
print(f"El valor retornado de ('mango', 5) es: {return_value}")
print(f"El diccionario actualizado es: {fruits}\n")