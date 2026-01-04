'''Utilizando ciclos for y while con conjuntos'''
nums = {1, 2, 3, 4, 5}
print(nums)

#Recorrer con el ciclo for
for element in nums:
    print(element)
print()

#Recorrer con el ciclo while
nums_lista = list(nums)
indice = 0

while indice < len(nums_lista):
    print(nums_lista[indice])
    indice += 1
