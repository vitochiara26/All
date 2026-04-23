arreglo = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    try:
        num_buscado = int(input("Ingrese el numero que desea buscar en el arreglo: "))
        break
    except Exception:
        print("Debes ingresar solo numeros enteros")

num_encontrado = False

for elemento in arreglo:
    if elemento == num_buscado:
        posicion = arreglo.index(elemento)
        print(f"El numero buscado ({num_buscado}) se encuentra en la posicion {posicion} del arreglo.")
        num_encontrado = True
        break

if not num_encontrado:
    print(f"El numero buscado ({num_buscado}) NO se encuentra en el arreglo.")
