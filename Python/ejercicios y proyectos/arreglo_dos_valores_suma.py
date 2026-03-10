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

k = int(input("Ingrese el valor 'K' para conocer si 2 elementos lo suman: "))
elementos = True

for i in range(tamaño_arreglo-1):
    for j in range(i+1, tamaño_arreglo):
        if (arreglo[i] + arreglo[j]) == k:
            print(f"Verdadero: {arreglo[i]} + {arreglo[j]} = {k}")
            elementos = False
        
if elementos:
    print(f"Ninguno par de elementos en el arreglo suma {k}")
