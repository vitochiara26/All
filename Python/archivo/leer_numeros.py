def leerArchivo(ruta):
    archivo = open(ruta, 'r', encoding='utf-8') 
    numeros = archivo.read()
    archivo.close()
    numeros_str = numeros.split(" ")
    numeros_int = [0]*len(numeros_str)
    for num in range(len(numeros_str)):
        numeros_int[num] = int(numeros_str[num])
    return numeros_int


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


ruta_arch_uno = r'all\Python\archivo\archivo_uno.txt'
ruta_arch_dos = r'all\Python\archivo\archivo_dos.txt'

numeros_arch_uno = leerArchivo(ruta_arch_uno)
numeros_arch_dos = leerArchivo(ruta_arch_dos)

merge_numeros = [0]*(len(numeros_arch_uno) + len(numeros_arch_dos))

indice_prin = indice_sec = 0

for num in range(len(merge_numeros)):        
        if num < len(numeros_arch_uno):
            merge_numeros[num] = numeros_arch_uno[indice_prin]
            indice_prin += 1
        else:
            merge_numeros[num] = numeros_arch_dos[indice_sec]
            indice_sec += 1

print(merge_numeros)

merge_numeros = ordenarArregloAscendente(merge_numeros)

print(merge_numeros)




