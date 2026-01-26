"""Traduce las siguientes expresiones
 matemáticas en forma de expresiones algorítmicas:"""

#Expresion 1
r = 5
pi = 3.1416
area_circulo = pi * r**2
print("Expresion 1")
print(f"El area del circulo es: {area_circulo}\n")

#Expresion 2
a, b = 0, 0
x, y = 3, 4
r = ((x - a)**2 + (y - b)**2)**0.5
print("Expresion 2")
print(f"El radio o la distancia es: {r}\n")

#Expresion 3
a, b = 2, 1
x, y = 6, 4
r = 4
valor = x**2 + y**2 - 2*a*x - 2*b*y + a**2 + b**2 - r**2
print("Expresion 3")
print(f"Resultado de la ecuacion: {valor}\n")

#Expresion 4
x, c, y = 5, 3, 9
valor_2a = ((x + c)**2 + (y - 0)**2)**0.5 + ((x - c)**2 + (y - 0)**2)**0.5
print("Expresion 4")
print(f"Resultado de la ecuacion: {valor_2a}\n")

#Expresion 5
a, b = 5, 3
p, q = 0, 0
x, y = 5, 0

valor_1 = ((x - p)**2 / a**2) + ((y - q)**2 / b**2)
print("Expresion 5")
print(f"Resultado de la ecuacion: {valor_1}\n")

#Expresion 6
b_uno = 10
b_dos = 6
h = 5

valor_A = ((b_uno + b_dos) / 2)*h
print("Expresion 6")
print(f"Valor del area de un trapecio: {valor_A}\n")