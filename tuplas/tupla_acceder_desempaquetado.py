'''Desempaquetado de tuplas'''
vowels_tuple = ("a", "e", "i", "o", "u")
print(vowels_tuple, '\n')
v1, v2 , v3 = vowels_tuple[:3]
print(v1, v2, v3, '\n')

countries_tuple = ("Mexico", "Brasil", "Argentina", "España")
print(countries_tuple, '\n')

p1, p2, p3 = countries_tuple[:3]
print("Desempaquetado de tupla [:3]")
print(f"Primer pais: {p1}")
print(f"Segundo pais: {p2}")
print(f"Tercer pais: {p3}")
