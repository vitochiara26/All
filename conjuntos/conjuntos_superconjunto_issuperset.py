'''superset y el metodo issuperset()'''
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {2, 5}

print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿A es superconjunto de B?:")

es_superconjunto = conjunto_a.issuperset(conjunto_b)
print("Utilizando el metodo issuperset:", es_superconjunto)

es_superconjunto = conjunto_a >= conjunto_b
print("Utilizando el operador >= :", es_superconjunto)

es_superconjunto = conjunto_a > conjunto_b
print("Utilizando el operador > :", es_superconjunto, "\n")

conjunto_b = {-3, 5}
print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿A es superconjunto de B?:")

es_superconjunto = conjunto_a.issuperset(conjunto_b)
print("Utilizando el metodo issuperset:", es_superconjunto)

es_superconjunto = conjunto_a >= conjunto_b
print("Utilizando el operador >= :", es_superconjunto)

es_superconjunto = conjunto_a > conjunto_b
print("Utilizando el operador > :", es_superconjunto, "\n")

conjunto_b = {1, 2, 3, 4, 5}
print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿A es superconjunto de B?:")

es_superconjunto = conjunto_a.issuperset(conjunto_b)
print("Utilizando el metodo issuperset:", es_superconjunto)

es_superconjunto = conjunto_a >= conjunto_b
print("Utilizando el operador >= :", es_superconjunto)

es_superconjunto = conjunto_a > conjunto_b
print("Utilizando el operador > :", es_superconjunto, "\n")