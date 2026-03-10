def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b > 0:
        a / b
    else :
        print("\nImposible dividir entre cero")

print("Calculadora bodegera")
print("--------------------")
operacion_valida = True

while operacion_valida:
    print("Presione 1 para sumar\nPresione 2 para restar\nPresione 3 para multiplicar\nPresione 4 para dividir")
    operacion = input()
    if operacion in ("1","2","3","4"):
        operacion_valida = False
    else :
        print("Opcion invalida")

x = int(input("\nIngrese el primer valor de su operacion: "))
y = int(input("Ingrese el segundo valor de su operacion: "))

if operacion == "1":
    resultado = sumar(x,y)
    print(f"\nEl resultado de la suma de {x} y {y} es: {resultado}")
elif operacion == "2":
    resultado = restar(x,y)
    print(f"\nEl resultado de la resta de {x} y {y} es: {resultado}")
elif operacion == "3":
    resultado = multiplicar(x,y)
    print(f"\nEl resultado de la multiplicación de {x} por {y} es: {resultado}")
else:
    resultado = dividir(x,y)
    print(f"\nEl resultado de la división de {x} entre {y} es: {resultado}")
