'''interseccion y el metodo intersection()'''
#conjuntoA.intersetcion(conjuntoB)
#ConjuntoA & ConjuntoB
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7 ,8}

print(f"{conjunto_A}\n{conjunto_B}\n")

#Utilizando el metodo intersection()
print(conjunto_A.intersection(conjunto_B))

#Utilizando el operardor &
print(conjunto_B & conjunto_A)
