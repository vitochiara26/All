'''el modulo random'''
import random
#randint(), devuelve un entero aleatorio en el rango [a, b]
num = random.randint(1, 100)
print("num = random.randint(1, 100)", num)

#random(), devuelve un numero de punto flotante en el rango [0.0 , 1.0]
num = random.random()
print("num = random.random():", num)

#randrange(), devuelve un elemento aleatorio de la secuencia generada por range
num = random.randrange(0, 100, 2)
print("num = random.ran(0, 100, 2):", num)