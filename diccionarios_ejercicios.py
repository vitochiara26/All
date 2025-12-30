'''Ejercicios para reforzar los conocimientos de diccionarios'''
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }


print("Ejercicio #1:")
print(fruits)
#alternativa 1 con el metodo get()
num_manzanas = fruits.get("manzanas")
print(f"Cantidad de manzanas con el metodo get(): {num_manzanas}")

#alternativa 2 consultando el valor
num_manzanas = fruits["manzanas"]
print(f"Cantidad de manzanas consultando el valor: {num_manzanas}")


print("\nEjercicio #2:")
#mi altenativa con el metodo update
print(fruits)
fruits.update({"bananas": 5,
               "mangos": 6,
               "uvas": 3
               })
print(f"Metodo update(): {fruits}")

#alternativa agregando elementos y su valor
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
fruits["bananas"] = 5
fruits["mangos"] = 6
fruits["uvas"] = 3
print(f"Asignando valor: {fruits}")


#alternativa metodo setdefault
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
fruits.setdefault("bananas", 5)
fruits.setdefault("mangos", 6)
fruits.setdefault("uvas", 3)
print(f"Metodo setdefault(): {fruits}")


print("\nEjercicio #3:")
#alteernativa metodo pop
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
fruits.pop("peras", "No se encuentra la clave")
print(f"Metodo pop: {fruits}")

#alternativa con funcion del
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
del fruits["peras"]
print(f"funcion del: {fruits}")


print("\nEjercicio #4:")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)

list_claves = list(fruits.keys())
print(f"Lista de claves: {list_claves}")
list_valores = list(fruits.values())
print(f"Lista de valores: {list_valores}")

print("\nEjercicio #5:")
fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
print("La clave manzanas existe en el diccionario?:")

if "manzanas" in fruits:
    print(True)
else:
    print(False)

fruits = {"uvas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)
print("La clave manzanas existe en el diccionario?:")
if "manzanas" in fruits:
    print(True)
else:
    print(False)
