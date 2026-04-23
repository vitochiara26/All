from datetime import datetime as t
time1 = t.now()

arreglo = [4, 3, 1, 5, 2, 8, 6, 9, 7]

for i in range(len(arreglo)):

    numero_mas_pequeño = arreglo[i]
    pos_numero_mas_pequeño = i

    for j in range(i+1,len(arreglo)):

        if arreglo[j] < numero_mas_pequeño:
            numero_mas_pequeño = arreglo[j]
            pos_numero_mas_pequeño = j

    arreglo[pos_numero_mas_pequeño] = arreglo[i]
    arreglo[i] = numero_mas_pequeño
    print(arreglo)

time2 = t.now()
tiempo = time2 - time1
print(tiempo)