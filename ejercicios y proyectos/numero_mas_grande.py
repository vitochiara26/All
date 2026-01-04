print("Programa para determinar cual es el numero mas grande de tres numeros.")

num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))
num_tres = int(input("Introduce el tercer numero: "))

if num_uno > num_dos and num_uno > num_tres :
    print("El numero " + str(num_uno) + " es el numero mas grande de los tres.")
    
elif num_dos > num_uno and num_dos > num_tres :
    print("El numero " + str(num_dos) + " es el numero mas grande de los tres.")
    
elif num_tres > num_uno and num_tres > num_dos :
    print("El numero " + str(num_tres) + " es el numero mas grande de los tres.")
     
