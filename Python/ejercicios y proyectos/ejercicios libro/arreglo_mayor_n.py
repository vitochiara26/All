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

n = int(input("Ingrese un valor para conocer cuantos elementos son mayor: "))

conteo_mayores = 0
suma_mayores = 0

for i in arreglo:
    if i > n:
        conteo_mayores += 1
        suma_mayores += i

if conteo_mayores == 0:
    print(f"No hay elementos en el arreglo mayores a {n}")
else :
    print(f"Hay {conteo_mayores} elementos en el arreglo mayores a {n}")
    print(f"Y su promedio es {suma_mayores/conteo_mayores}")