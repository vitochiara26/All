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
pos_mayor = 0
for i in range(tamaño_arreglo):
    for j in range(i+1,tamaño_arreglo):
        if arreglo[i] > arreglo[j]:
            if arreglo[pos_mayor] < arreglo[i]:
                pos_mayor = i
        elif arreglo[j] > arreglo[i]:
            if arreglo[pos_mayor] < arreglo[j]:
                pos_mayor = j

print(f"El elemento mayor en el arreglo es {arreglo[pos_mayor]}")