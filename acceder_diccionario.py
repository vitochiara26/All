'''accediendo a los elementos de un diccionario'''
dictionary = {"a": 1,
              "e": 2,
              }

print(dictionary)
print(f"Clave a: {dictionary['a']}")
print(f"Clave e: {dictionary['e']}")

print()

dictionary = {"numbers": [18,20,28],
              "groups": {"a": 1,"b": 2},
              }

print(dictionary)
print(f"Clave numbers: {dictionary['numbers']}")
print(f"Clave groups: {dictionary['groups']}")

print(f"Clave numbers: {dictionary['numbers'][1]}")
print(f"Clave groups: {dictionary['groups']['b']}")

print()
