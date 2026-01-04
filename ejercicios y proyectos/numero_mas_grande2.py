print("Programa para determinar cual es el numero mas grande de tres numeros.")

nu = int(input("Introduce el primer numero: "))
nd = int(input("Introduce el segundo numero: "))
nt = int(input("Introduce el tercer numero: "))

if nu > nd and nu > nt :
    print("El numero " + str(nu) + " es el numero mas grande de los tres.")
elif nd > nt :
    print("El numero " + str(nd) + " es el numero mas grande de los tres.")
else :
    print("El numero " + str(nt) + " es el numero mas grande de los tres.")
