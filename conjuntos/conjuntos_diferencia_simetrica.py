'''Diferencia simetrica entre conjuntos y el metodo symmetric_difference()'''
#conjuntoA.symmetric_difference(conjuntoB)
#ConjuntoA ^ ConjuntoB
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7 ,8}

print(f"{conjunto_A}\n{conjunto_B}\n")

#Utilizando el metodo symmetrix_difference()
print(conjunto_A.symmetric_difference(conjunto_B))
print(conjunto_B.symmetric_difference(conjunto_A))

#Utilizando el operardor ^
print(conjunto_B ^ conjunto_A)
print(conjunto_A ^ conjunto_B)
