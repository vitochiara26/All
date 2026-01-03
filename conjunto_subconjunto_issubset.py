'''subconjuntos y el metodo issubset()'''
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {2, 4}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_b = {2, 8}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
