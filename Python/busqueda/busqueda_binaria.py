arreglo = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

indice_inicial = 0
indice_final = len(arreglo) -1
indice_central = indice_final // 2

while True:
    try:
        num_buscado = int(input("Ingrese el numero que desea buscar en el arreglo: "))
        break
    except Exception:
        print("Debes ingresar solo numeros enteros")
centro_anterior = -1
centro_actual = -2
numero_encontrado = False

while centro_anterior != centro_actual:
    centro_anterior = indice_central

    if arreglo[indice_central] == num_buscado:
        print(f"El numero buscado ({num_buscado}) se encuentra en la posicion {indice_central} del arreglo.")
        numero_encontrado = True
        break
    else:
        if num_buscado > arreglo[indice_central]:
            indice_inicial = indice_central + 1
            indice_central = ((indice_final - indice_inicial) // 2) + indice_inicial
        else:
            indice_final = indice_central - 1
            indice_central = indice_final // 2

    centro_actual = indice_central

if not numero_encontrado:
        print(f"El numero buscado ({num_buscado}) NO se encuentra en el arreglo.")
