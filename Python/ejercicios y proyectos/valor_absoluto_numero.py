num = float(input("Introduce un numero (positivo/negativo/entero/decimal): "))

if num < 0 :
    num *= (-1)

print(f"El valor absoluto del numero ingresado es {num}")
