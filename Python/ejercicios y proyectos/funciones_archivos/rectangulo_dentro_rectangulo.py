import funcion_rectangulo as fr

print("En este programa crearemos dos rectangulos para luego determinar si" \
" algun vertice del primer rectangulo esta dentro del segundo.")

print("Ingrese las coordenadas del vertice superior izquierdo del", end=" ")
vertice_sup_izq_r1 = input("primer rectangulo separados para una coma (X,Y): ").split(",")
vertice_sup_izq_r1[0] = int(vertice_sup_izq_r1[0])
vertice_sup_izq_r1[1] = int(vertice_sup_izq_r1[1])
pos_x_uno_r1 = vertice_sup_izq_r1[0]
pos_y_dos_r1 = vertice_sup_izq_r1[1]
ancho_r1 = int(input("Cual es el ancho del primer rectangulo: "))
print("Cual es la altura del primer rectangulo, (recuerda que", end=" ")
alto_r1 = int(input("debe ser mayor o menor al ancho, nunca igual): "))
pos_x_dos_r1 = pos_x_uno_r1 + ancho_r1
pos_y_uno_r1 = pos_y_dos_r1 - alto_r1

#vert_sup_izq_r1 = [pos_x_uno_r1, pos_y_dos_r1]
#vert_sup_der_r1 = [pos_x_dos_r1, pos_y_dos_r1]
#vert_inf_der_r1 = [pos_x_dos_r1, pos_y_uno_r1]
#vert_inf_izq_r1 = [pos_x_uno_r1, pos_y_uno_r1]

print("Ingrese las coordenadas del vertice superior izquierdo del", end=" ")
vertice_sup_izq_r2 = input("segundo rectangulo separados para una coma (X,Y): ").split(",")
vertice_sup_izq_r2[0] = int(vertice_sup_izq_r2[0])
vertice_sup_izq_r2[1] = int(vertice_sup_izq_r2[1])
pos_x_uno_r2 = vertice_sup_izq_r2[0]
pos_y_dos_r2 = vertice_sup_izq_r2[1]
ancho_r2 = int(input("Cual es el ancho del segundo rectangulo: "))
print("Cual es la altura del segundo rectangulo, (recuerda que", end=" ")
alto_r2 = int(input("debe ser mayor o menor al ancho, nunca igual): "))
pos_x_dos_r2 = pos_x_uno_r2 + ancho_r2
pos_y_uno_r2 = pos_y_dos_r2 - alto_r2

vert_1_dentro = fr.comprobar_punto_dentro_fuera(pos_x_uno_r2, pos_x_dos_r2, pos_y_uno_r2, pos_y_dos_r2, pos_x_uno_r1, pos_y_dos_r1)
vert_2_dentro = fr.comprobar_punto_dentro_fuera(pos_x_uno_r2, pos_x_dos_r2, pos_y_uno_r2, pos_y_dos_r2, pos_x_dos_r1, pos_y_dos_r1)
vert_3_dentro = fr.comprobar_punto_dentro_fuera(pos_x_uno_r2, pos_x_dos_r2, pos_y_uno_r2, pos_y_dos_r2, pos_x_dos_r1, pos_y_uno_r1)
vert_4_dentro = fr.comprobar_punto_dentro_fuera(pos_x_uno_r2, pos_x_dos_r2, pos_y_uno_r2, pos_y_dos_r2, pos_x_uno_r1, pos_y_uno_r1)

if vert_1_dentro and vert_2_dentro and vert_3_dentro and vert_4_dentro:
    print("Todos los vertices del primer rectangulo estan dentro del segundo")
elif vert_1_dentro and vert_2_dentro :
    print("Los vertices uno y dos (el borde superior) del primer rectangulo estan dentro del segundo")
elif vert_2_dentro and vert_3_dentro :
    print("Los vertices dos y tres (el borde derecho) del primer rectangulo estan dentro del segundo")
elif vert_3_dentro and vert_4_dentro : 
    print("Los vertices tres y cuatro (el borde inferior) del primer rectangulo estan dentro del segundo")
elif vert_1_dentro and vert_4_dentro :
    print("Los vertices uno y cuatro (el borde izquierdo) del primer rectangulo estan dentro del segundo")
elif vert_1_dentro :
    print("El vertice uno (esquina superior izquierda) del primer rectangulo está dentro del segundo")
elif vert_2_dentro :
    print("El vertice dos (esquina superior derecha) del primer rectangulo está dentro del segundo")
elif vert_3_dentro :
    print("El vertice tres (esquina inferior derecha) del primer rectangulo está dentro del segundo")
elif vert_4_dentro :
    print("El vertice cuatro (esquina inferior izquierda) del primer rectangulo está dentro del segundo")
else:
    print("Ningun vertice del primer rectangulo se encuentra dentro del segundo")
