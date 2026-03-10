import funcion_rectangulo as fr

print("En este programa crearemos un rectangulo para luego " \
"determinar si un punto dado esta dentro o fuera")
print("Ingrese las coordenadas del vertice superior izquierdo", end=" ")
vertice_sup_izq = input("separados para una coma (X,Y): ").split(",")
vertice_sup_izq[0] = int(vertice_sup_izq[0])
vertice_sup_izq[1] = int(vertice_sup_izq[1])
pos_x_uno = vertice_sup_izq[0]
pos_y_dos = vertice_sup_izq[1]

ancho = int(input("Cual es el ancho del rectangulo: "))
print("Cual es la altura del rectangulo, (recuerda que", end=" ")
alto = int(input("debe ser mayor o menor al ancho, nunca igual): "))

pos_x_dos = pos_x_uno + ancho
pos_y_uno = pos_y_dos - alto

print("Ingrese dos valores, 'X' y 'Y'", end=" ")
punto = input("separados para una coma: ").split(",")
punto[0] = int(punto[0])
punto[1] = int(punto[1])

mensaje = fr.comprobar_punto_dentro_fuera(pos_x_uno, pos_x_dos, pos_y_uno, pos_y_dos, punto[0], punto[1])
if mensaje is True:
    print("El punto indicado 'SI' se encuentra dentro del rectangulo.")
else:
    print("El punto indicado 'NO' se encuentra dentro del rectangulo.")
