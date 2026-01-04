'''subconjuntos y el metodo issubset()'''
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {2, 4}

print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿B es subconjunto de A?:")

es_subconjunto = conjunto_b.issubset(conjunto_a)
print("Utilizando el metodo issubset:", es_subconjunto)

es_subconjunto = conjunto_b <= conjunto_a
print("Utilizando el operador <= :", es_subconjunto)

es_subconjunto = conjunto_b < conjunto_a
print("Utilizando el operador < :", es_subconjunto, "\n")

conjunto_b = {2, 0}

print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿B es subconjunto de A?:")

es_subconjunto = conjunto_b.issubset(conjunto_a)
print("Utilizando el metodo issubset:", es_subconjunto)

es_subconjunto = conjunto_b <= conjunto_a
print("Utilizando el operador <= :", es_subconjunto)

es_subconjunto = conjunto_b < conjunto_a
print("Utilizando el operador < :", es_subconjunto, "\n")

conjunto_b = {3, 4, 2 , 5, 1}

print(f"Conjunto A: {conjunto_a}\nConjunto B: {conjunto_b}")
print("¿B es subconjunto de A?:")

es_subconjunto = conjunto_b.issubset(conjunto_a)
print("Utilizando el metodo issubset:", es_subconjunto)

es_subconjunto = conjunto_b <= conjunto_a
print("Utilizando el operador <= :", es_subconjunto)

es_subconjunto = conjunto_b < conjunto_a
print("Utilizando el operador < :", es_subconjunto, "\n")
