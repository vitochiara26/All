posicion = 0
tamaño_arreglo = int(input(f"Ingrese el tamaño del arreglo: "))
valor = int(input(f"Ingrese el valor #{posicion+1}: "))
arreglo = [0]*tamaño_arreglo
arreglo[posicion] = valor
aux = 0

while posicion < tamaño_arreglo-1 :
    posicion +=1
    valor = int(input(f"Ingrese el valor #{posicion+1}: "))
    arreglo[posicion] = valor

print(f"Arreglo original: {arreglo}")

k = int(input("Ingrese el valor 'K' para mover circulamente el arreglo: "))

if k == tamaño_arreglo:
    print(f"Arreglo movido: {arreglo}")
else :
    if k > tamaño_arreglo:
        k = k % tamaño_arreglo
    for i in range(k):
        i = 0
        aux = arreglo[i]
        for j in range(tamaño_arreglo-1):
            arreglo[j] = arreglo[j+1]
        arreglo[tamaño_arreglo-1] = aux

print(f"Arreglo movido: {arreglo}")
