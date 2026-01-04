'''El metodo keys en diccionarios'''
dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }

print(dictionary)
print(f"\nLas keys del diccionario son:\n{dictionary.keys()}")

print("\nConvirtiendo keys a lista utilizando el constructor list()")
list_keys = list(dictionary.keys())

print(f"La lista es: {list_keys}")
print(f"Posicion 1 de la lista keys: {list_keys[1]}")
