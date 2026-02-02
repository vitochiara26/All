suma = 0
nota = 0
valid_nota = False
alumnos = int(input("Ingrese la cantidad de estudiantes en su curso: "))

for i in range(1, alumnos +1):
    nota = float(input(f"Ingrese la nota del estudiante #{i}: "))

    while valid_nota is False:
        if nota > 0 and nota < 20 :
            valid_nota = True
        else :
            print("Ingrese un nota entre 0 y 20")
            nota = float(input(f"Ingrese la nota del estudiante #{i}: "))
    valid_nota = False
    
    suma += nota

promedio = suma/10
print(f"El promedio de las notas de todos los estudiantes es {promedio}")
