# Proyecto de propagacion de fuego en un bosque 
import funciones_bosque as fb
import time as t

# El programa pide al usuario que ingrese el tamaño del bosque, la cantidad de llamas y la cantidad 
# de turnos para ver la propagacion del fuego. Luego, se crea el bosque con arboles, objetos no 
# quemables y llamas, y se muestra en pantalla. Finalmente, se simula la propagacion del fuego 
# durante los turnos indicados por el usuario, mostrando el estado del bosque en cada turno.

while True:
    # Solicitamos al usuario que ingrese la cantidad de filas que tendra el bosque, validando que 
    # sea un numero entero entre 1 y 100.
    while True:
        try:
            filas = int(input("Ingrese un numero entero menor " \
            "a 100 para definir el ancho del bosque: "))
        except Exception:
            print("Debe ingresar solo valores numericos.")
            continue
        if 0 < filas <= 100:
            break
        else:
            print("Debe ingresar un numero entero mayor a 0 y menor a 100")

    # Solicitamos al usuario que ingrese la cantidad de columnas que tendra el bosque, validando que
    # sea un numero entero entre 1 y 100.
    while True:
        try:
            columnas = int(input("Ingrese otro numero entero menor " \
            "a 100 para definir lo largo del bosque: "))
        except Exception:
            print("Debe ingresar solo valores numericos.")
            continue
        if 0 < columnas <= 100:
            break
        else:
            print("Debe ingresar un numero entero mayor a 0 y menor a 100")

    # Solicitamos al usuario que ingrese la cantidad de llamas que desea crear dentro del bosque, 
    # validando 
    while True:
        limite_llamas = (filas * columnas) // 4
        if limite_llamas > 10:
            limite_llamas = 10
        print("Ingrese la cantidad de llamas que deseas crear dentro del bosque")
        try:
            cantidad_llamas = int(input(f"Puedes crear entre 1 a {limite_llamas} llamas: "))
        except Exception:
            print("Debe ingresar solo valores numericos.")
            continue
        if 1 <= cantidad_llamas <= limite_llamas:
            break
        else:
            print(f"Debe ingresar un numero de llamas mayor a 0 y menor a {limite_llamas}")
        
    # Solicitamos al usuario que ingrese la cantidad de turnos para ver la propagacion del fuego, 
    # validando que sea un numero entero entre 2 y 50. El minimo de 2 turnos es para poder ver la 
    # propagacion del fuego, y el maximo de 50 turnos es para evitar que el programa se vuelva muy
    # extenso.
    while True:
        print("En cuantos turnos deseas ver la propagacion de la llamas?")
        try:
            turnos = int(input("Debe ser un minimo de 2 turnos y maximo 50 turnos: "))
        except Exception:
            print("Debe ingresar solo valores numericos.")
            continue
        if 2 <= turnos <= 50: 
            break
        else:
            print("Debe ingresar un numero de turnos mayor a 2 y menor a 50")
    break

# Creamos el bosque con arboles.
bosque = fb.rellenarMatrizArboles(filas, columnas)

# Creamos el bosque con objetos no quemables.
bosque = fb.crearNoQuemables(filas, columnas, bosque)

# Creamos el bosque con llamas.
bosque = fb.crearLlamas(cantidad_llamas, filas, columnas, bosque)

# Mostramos el bosque con emojis.
print(fb.mostrarMatrizBosqueEmojis(bosque))

# Simulamos la propagacion del fuego durante los turnos indicados por el usuario, mostrando el 
# estado del bosque en cada turno.
turno = 0
while turno <= turnos:
    bosque = fb.incrementarLLamas(filas, columnas, bosque)
    bosque = fb.propagacionLlamas(filas, columnas, bosque)
    print(f"Turno #{turno} \n")
    print(fb.mostrarMatrizBosqueEmojis(bosque))
    turno += 1
    t.sleep(0.85)
    
    # Verificamos si aun hay fuego en el bosque, contando la cantidad de llamas en cada estado 
    # (0, 1, 2 y 3). Si no hay llamas en ningun estado, significa que el fuego se ha extinguido por 
    # completo y no hay mas arboles quemables.

    aun_hay_fuego_0 = 0
    aun_hay_fuego_1 = 0
    aun_hay_fuego_2 = 0
    aun_hay_fuego_3 = 0

    for fila in bosque:
        for columna in fila:
            if columna == "  0":
                aun_hay_fuego_0 += 1
            if columna == "  1":
                aun_hay_fuego_1 += 1
            if columna == "  2":
                aun_hay_fuego_2 += 1
            if columna == "  3":
                aun_hay_fuego_3 += 1

    # Si no hay llamas en ningun estado, significa que el fuego se ha extinguido por completo y 
    # finalizamos el programa.
    if aun_hay_fuego_0 == 0 and aun_hay_fuego_1 == 0 and aun_hay_fuego_2 == 0 and aun_hay_fuego_3 == 0:
        print("El fuego se ha extinguido en su totalidad y no hay mas quemables.")
        break


