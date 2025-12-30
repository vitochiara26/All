print("Introduce dos numeros a comparar:\n")

num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))

print("\nLos numeros a comparar son: " , num_uno , " y " , num_dos , "\n")

if num_uno == num_dos :
    print("Es igual...")
else :
    print("Es diferente...")

if num_uno > num_dos :
    print("Es mayor...")
elif num_uno < num_dos :
    print("Es menor....")
else :
    print("Es igual...")

if num_uno <= num_dos :
    print("Es menor o igual")
else :
    print("Es mayor o igual")
