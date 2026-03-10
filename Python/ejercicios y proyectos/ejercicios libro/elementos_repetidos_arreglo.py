posicion = 0
tamaño_arreglo = int(input(f"Ingrese el tamaño del arreglo: "))
valor = int(input(f"Ingrese el valor #{posicion+1}: "))
arreglo = [0]*tamaño_arreglo
arreglo[posicion] = valor

while posicion < tamaño_arreglo-1 :
    posicion +=1
    valor = int(input(f"Ingrese el valor #{posicion+1}: "))
    arreglo[posicion] = valor

print(f"Arreglo original: {arreglo}")
array_contador = [0]*101

for num in arreglo:
    array_contador[num] += 1


array_mayor = -1
mas_repetido = 0
for pos in range(len(array_contador)):
    if array_contador[pos] > array_mayor:
        array_mayor = array_contador[pos]
        mas_repetido = pos

repetidos = 0
for repeticiones in array_contador:
    if repeticiones == array_mayor:
        repetidos += 1

if array_mayor <= 1:
    print("No hay repeticiones de ningun valor.")
elif repetidos == 1:
    print(f"El numero mas repetido fue el {mas_repetido}, se repite {array_mayor} veces.")
else:
    print(f"Los numeros mas repetidos fueron: ", end="")
    for pos in range(len(array_contador)):
        if array_contador[pos] == array_mayor:
            print(f"{pos}", end=", ")
    print(f" se repiten {array_mayor} veces cada uno.")