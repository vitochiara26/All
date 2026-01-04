'''Diccionarios'''
nombre_diccionario = {"a": "hola", "b": [0,1,2] , "c": 3 , "d": {"a": 1}}
#Diccionario vacio
dictionary_empty = {}
print(f"Diccionario vacio: {dictionary_empty}")
print()

#Diccionario homogeneo
dictionary_ages = {"Juan": 32,
                   "Gerardo": 21,
                   "Luis": 25
                   }

print(f"Diccionario de edades: {dictionary_ages}")
print()

#Diccionario heterogeneo
dictionary_dates = {"name": "Brenda",
                    "last_name": "Flores",
                    "age": 22,
                    }

print(f"Diccionario de edades: {dictionary_dates}")
print()

#Un diccionario puede almacenar listas y diccionarios
dictionary_list = {"a": {"a": 1},
                   "b": [0,1,2],
                   }
print(f"Diccionario con lista y diccionario: {dictionary_list}")
print()

#Un diccionario puede tener claves numericas
dictionary_keys_num = {4: 1,
                       5: 2,
                       6: 3,
                       }

print(f"Diccionario con claves numericas {dictionary_keys_num}")
print()

#Un diccionario no puede tener calves repetidas
dictionary_repeated_keys = {"Juan": 20,
                            "Gerardo": 30,
                            "Juan": 15,
                            }

print(f"Diccionario con claves repetidas: {dictionary_repeated_keys}")
print()

#Un diccionario puede tener claves numericas o de tipo texto
dictionary ={1: 23,
             "Juan": 5,
             -2: "hola"
             }

print(f"Diccionario con claves de distintos tipos de dato: {dictionary}")
