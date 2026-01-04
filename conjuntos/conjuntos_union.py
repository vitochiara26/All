'''union y el metodo union()'''
#conjuntoA.union(conjuntoB)
#ConjuntoA | ConjuntoB
conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}

print(f"{conjunto_A}\n{conjunto_B}\n")

#Utilizando el metodo union()
print(conjunto_A.union(conjunto_B))

#Utilizando el operardor |
print(conjunto_B | conjunto_A)
