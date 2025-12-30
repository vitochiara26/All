'''El metodo get() para consultar valores de claves'''
dict_name = {"a": 1,
             "b": 2,
             "c": 3
             }
print(dict_name.get("a"))
print(dict_name.get("b"))
print(dict_name.get("c", 4))
print(dict_name.get("z", 4))

fruits_dict = {"manzana": 1.55,
               "banana": 3.55,
               "naranja": 1.25,
               }
print(fruits_dict)

precio_manzana = fruits_dict.get("manzana")
print(f"El precio de la manzana es: {precio_manzana}")

precio_mango = fruits_dict.get("mango")
print(f"El precio del mango es: {precio_mango}")

precio_mango = fruits_dict.get("mango", 4.55)
print(f"El precio del mango es: {precio_mango}")