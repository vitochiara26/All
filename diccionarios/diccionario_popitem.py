'''El metodo popitem() para eliminar y almacenar el ultimo item de un diccionario'''
dictionary = {"a": 1,
             "b": 2,
             "c": 3
             }
print(dictionary)

item = dictionary.popitem()

print(f"El item eliminado es: {item}")
print(dictionary)
