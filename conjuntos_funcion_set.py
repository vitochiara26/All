'''Inicio de leccion sobre conjuntos y la funcion set() en Python'''
print("Conjuntos creados con llaves {}:")

print("Ejmeplo #1: {5, 1, 3, 2, 4}")
conjunto = {5, 1, 3, 2, 4}
print(conjunto, "\n")

print("Ejemplo #2: {-1, 0, 5, -2, 1, 4}")
conjunto = {-1, 0, 5, -2, 1, 4}
print(conjunto, "\n")

print("Ejemplo #3: {'e','o', 'a', 'u', 'i'}")
conjunto = {'e','o', 'a', 'u', 'i'}
print(conjunto, "\n")

print("Ejmplo #4: {'e', 5, 'o', 0, 'a', 2, -1}")
conjunto = {'e', 5, 'o', 0, 'a', 2, -1}
print(conjunto, "\n")

print("Ejemplo #5: {5, 1, 1, 1, 3, 5}")
conjunto = {5, 1, 1, 1, 3, 5}
print(conjunto, "\n")

print("Ejemplo #6: {5, (3, 2, 4), 1, 0, 6}")
conjunto = {5, (3, 2, 4), 1, 0, 6}
print(conjunto, "\n")

print("Ejemplos con la funcion set(): \n")

print("Ejemplo #7: ['e', 5, 'o', 0, 'a', 2, -1]")
lista = ['e', 5, 'o', 0, 'a', 2, -1]
conjunto = set(lista)
print(conjunto, "\n")

print("Ejemplo #8: String 'Hola'")
conjunto = set("Hola")
print(conjunto)
