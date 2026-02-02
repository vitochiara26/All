print("Programa para determinar el signo de una suma calcular la operacion: ")
num_uno = float(input("Ingrese el primer valor: "))
num_dos = float(input("Ingrese el segundo valor: "))

if (num_uno < 0 and num_dos < 0) or (num_uno >= 0 and num_dos >= 0) :
    print("El signo de la suma es positivo (+)")
else :
    print("El signo de la suma es negativo (-)")

