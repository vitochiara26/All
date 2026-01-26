"""Dado a, b, c imprime x"""

a = int(input("Introduce el valor de la variable a: "))
b = int(input("Introduce el valor de la variable b: "))
c = int(input("Introduce el valor de la variable c: "))

x_uno = (-b + ((b**2) - (4*a*c))**0.5) / (2*a)
x_dos = (-b - ((b**2) - (4*a*c))**0.5) / (2*a)

print(f"Los valores resultantes serian: {x_uno} | {x_dos} ")