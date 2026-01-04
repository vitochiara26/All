'''El metodo update() para actualizar o agregar un diccionario a otro'''
dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }
print(f"Diccionario original: {dict_name}")

dict_name.update({"z": 4, "d": 5})
print(f"Agregando 'z' y 'd': {dict_name}")

dict_name.update({"a": 6, "b": 5})
print(f"Actualizando 'a' y 'b': {dict_name}")