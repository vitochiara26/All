suma_impares = 0
conteo_impares = 0

suma_pares = 0
conteo_pares = 0

suma_total = 0
conteo_total = 0

print("Ingresa una secuencia de números. Escribe '0' para finalizar.")
print("-------------------------------------------------------------")

while True:
    try:
        num = int(input("Ingresa un numero: "))

        if num == 0:
            break

        suma_total += num
        conteo_total += 1

        if num % 2 == 0:
            suma_pares += num
            conteo_pares += 1
        else :
            suma_impares += num
            conteo_impares += 1
        
    except ValueError:
        print("Ingrese solo numeros enteros")

print("Resultados")
print("----------")

if conteo_total == 0:
    print()
else:
    porcent_par = (conteo_pares / conteo_total) * 100 
    porcent_impar = (conteo_impares / conteo_total) *100


    print(f"Numeros totales ingresados: {conteo_total}")
    print(f"Suma de todos los numeros ingresados: {suma_total}")
    print("----------------------------------------")
    print(f"Suma de todos los numeros pares: {suma_pares}")
    print(f"Porcentaje de numeros pares: {porcent_par:.2f}%")
    print("----------------------------------------")
    print(f"Suma de todos los numeros impares: {suma_impares}")
    print(f"Porcentaje de numeros impares: {porcent_impar:.2f}%")
