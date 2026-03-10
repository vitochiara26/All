def millas_km(distancia):
    distancia *= 1.6
    distancia = round(distancia, 1)
    return distancia


def leer_ciudades():
    mensaje = ""
    for i in entrada:
        for j in i:
            if  i.index(j) == 0 :
                mensaje += j.capitalize() + " "
            elif i.index(j) == 1:
                mensaje += j.capitalize() + ": "
            else :
                mensaje += str(j) + "\n"
    return mensaje


def ejecucion(ciudad_uno, ciudad_dos, distancia):
    if ciudad_uno == ciudad_dos and distancia == 0:
        return False
    return True


ejecution = True
entrada = []

while ejecution :
        fila_temporal = []
        for i in range(3):
            if i < 2:
                fila_temporal.append(input("Ingresa una ciudad: ").lower())
            else :
                distance = float(input("Ingresa la distancia en millas entres ambas ciudades: "))
                distance = millas_km(distance)
                fila_temporal.append(distance)
        final = ejecucion(fila_temporal[0], fila_temporal[1], fila_temporal[2])

        if final is True: 
            entrada.append(fila_temporal)
        else : 
            ejecution = final

mensaje_final = leer_ciudades()
print(mensaje_final)
