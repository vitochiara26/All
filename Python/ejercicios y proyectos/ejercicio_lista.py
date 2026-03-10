posicion = 0
valor = int(input(f"Ingrese el valor #{posicion+1}: "))
arreglo = [0]*16
arreglo[posicion] = valor

valor_final = 10
potencias_dos = [0]*valor_final
for i in range(0, valor_final):
    potencias_dos[i] = 2**i


while posicion < 15 :
    posicion +=1
    valor = int(input(f"Ingrese el valor #{posicion+1}: "))
    arreglo[posicion] = valor
print(potencias_dos)
print(f"Arreglo original: {arreglo}")

k = int(input("Ingrese el valor 'K' para reemplazar los valores que aja, ya sabemos...: "))

posicion = 0
for pos in range(0,len(arreglo)):
    if pos in potencias_dos:
        arreglo[posicion] = k
    posicion += 1

print(f"Arreglo modificado: {arreglo}")