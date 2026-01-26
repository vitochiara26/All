'''Contabibilizar los notas de un solo alumno en un sola materia'''
#examen1 20%, examen2 25%, examen 3 y 4 10%, examen5 35%
alumno = input("Ingrese el nombre del alumno: ")

nota_uno = float(input("Ingrese la nota del primer examen: "))
nota_dos = float(input("Ingrese la nota del segundo examen: "))
nota_tres = float(input("Ingrese la nota del tercer examen: "))
nota_cuatro = float(input("Ingrese la nota del cuarto examen: "))
nota_cinco = float(input("Ingrese la nota del quinto examen: "))

valor_nota_uno = nota_uno * 0.2
valor_nota_dos = nota_dos * 0.25
valor_nota_tres = nota_tres * 0.1
valor_nota_cuatro = nota_cuatro * 0.1
valor_nota_cinco = nota_cinco * 0.35

nota_final = valor_nota_uno + valor_nota_dos + valor_nota_tres + valor_nota_cuatro + valor_nota_cinco
print("Nota final del Alumno" , alumno , ":" , nota_final)
