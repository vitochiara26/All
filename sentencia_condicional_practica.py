print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, cual es tu nombre?: ")

matematicas = int(input(nombre + ", cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre + ", cual es tu calificacion en quimica?: "))
biologia = int(input(nombre + ", cual es tu calificacion en biologia?: "))

promedio = (matematicas + quimica + biologia) // 3

if promedio >= 6 :
    print('Felicidades ' + nombre + '. "aprobaste" con un promedio de: ', promedio)

print("Fin.")
