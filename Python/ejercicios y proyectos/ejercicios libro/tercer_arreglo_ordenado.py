arreglo_a = [1,4,6,9,11]
arreglo_b = [2,3,5,10,12]
arreglo_c = []

tam_a = len(arreglo_a)
tam_b = len(arreglo_b)
arreglo_menor = ""
arreglo_mayor = ""
tam_menor = 0
tam_mayor = 0

if tam_a > tam_b:
    tam_menor = tam_b
    tam_mayor = tam_a
    arreglo_mayor = "a"
else :
    tam_menor = tam_a
    tam_mayor = tam_b
    arreglo_mayor = "b"


count = 0
while count < tam_menor:
    if arreglo_a[count] < arreglo_b[count]:
        arreglo_c.append(arreglo_a[count])
        arreglo_c.append(arreglo_b[count])
        count += 1
    else:
        arreglo_c.append(arreglo_b[count])
        arreglo_c.append(arreglo_a[count])
        count += 1

if tam_menor != tam_mayor:
    while count < tam_mayor:
        if arreglo_mayor == "a":
            arreglo_c.append(arreglo_a[count])
            count += 1
        elif arreglo_mayor == "b":
            arreglo_c.append(arreglo_b[count])
            count += 1

print(arreglo_a)
print(arreglo_b)
print(arreglo_c)
