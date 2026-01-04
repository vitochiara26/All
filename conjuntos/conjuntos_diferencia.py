'''Diferencia entre conjuntos y el metodo difference()'''
#conjuntoA.difference(conjuntoB)
#ConjuntoA - ConjuntoB
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7 ,8}

print(f"{conjunto_A}\n{conjunto_B}\n")

#Utilizando el metodo difference()
print(conjunto_A.difference(conjunto_B))
print(conjunto_B.difference(conjunto_A))

#Utilizando el operardor -
print(conjunto_B - conjunto_A)
print(conjunto_A - conjunto_B)
