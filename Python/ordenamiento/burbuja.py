from datetime import datetime as t
time1 = t.now()

def ordenarArregloAscendente(arreglo):
    arreglito = []
    arreglito.extend(arreglo)
    for i in range(len(arreglito)):
        for j in range(i+1,len(arreglito)):
            if arreglito[i] > arreglito[j]: 
                caja_aux = arreglito[j]
                arreglito[j] = arreglito[i] 
                arreglito[i] = caja_aux
    return arreglito


def ordenarArregloDescendente(arreglo):
    arreglito = []
    arreglito.extend(arreglo)
    for i in range(len(arreglito)):
        for j in range(i+1,len(arreglito)):
            if arreglito[i] < arreglito[j]: 
                caja_aux = arreglito[j]
                arreglito[j] = arreglito[i] 
                arreglito[i] = caja_aux
    return arreglito


arreglo = [4, 3, 1, 5, 2, 8, 6, 9, 7]

print(arreglo)

arreglo_ordenado_ascend = ordenarArregloAscendente(arreglo)

print(arreglo_ordenado_ascend)

time2 = t.now()
tiempo = time2 - time1
print(tiempo)
