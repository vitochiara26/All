'''Como recorrer diccionarios usando el ciclo for'''
dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }

#Recorriendo unicamente las claves
for key in dict_name:
    print(f"{key} : {dict_name[key]}")
print()

#Recorriendo los items
for key, value in dict_name.items():
    print(f"{key} : {value}")
