'''El metodo copy() para duplicar nuevos diccionarios'''
dictionary = {"nombre": "Diego",
              "apellido": "Lozano",
              "edad": 25
              }

print(f"Diccionario original: {dictionary}")

dictionary_copy = dictionary.copy()
print(f"Diccionario copia: {dictionary_copy}")
