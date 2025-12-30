total_matrixs = int(input("cuantas matrices deseas sumar?: ")) #indica el numero de matrices que se van a crear

if total_matrixs > 1: #entra en bucle si las matrices a crear son 2 o mas
    filas = int(input("Cuantas filas tendran las matrices?: ")) #indica cuantas filas tendra cada matriz
    columnas = int(input("Cuantas columnas tendran las matrices?: ")) #indica cuantas columnas tendra cada matriz

    matrix_list = [] #matriz general vacia, donde se van a guardar todas las matrices creadas

    for matrix in range(total_matrixs): #bucle para crear cada matriz
        matrix_actual = [] #crea la matriz donde se guardaran los datos ingresados por el usuario
        for indice_fila in range(filas) : #bucle para crear la fila de la matriz
            lista_actual = [] #crea la lista donde se guardaran las columnas
            for indice_columna in range(columnas) : #bucle para crear los columnas 
                lista_actual.append(int(input(f"Introduce un elemento para la matriz {matrix + 1}, fila {indice_fila}, columna {indice_columna}: "))) 
                #'''print(lista_actual)'''
                #agrega a la fila en la que se encuentre en el indice_fila, en la columna del indice_columna, el elemento ingresado por el usuario
            matrix_actual.append(lista_actual) #inserta la fila creada a la matriz
            #'''print(matrix_actual)'''
        matrix_list.append(matrix_actual) #inserta la matriz generada a la lista donde estaran todas las matrices
        #'''print(matrix_list)'''
    

    matrix_actual = [] #resetea los elementos de la matriz 
    for indice_fila in range(filas): #ingresa a la fila de la matriz
        lista_actual = [] #crea la fila de la matriz nueva sumada
        for indice_columna in range(columnas): #ingresa a la columna de cada fila
            sum_matrix = 0 #crea una variable donde guardar el valor de las sumas
            for matrix_position in range(len(matrix_list)): #indica la matriz donde se encuentra dentro de la lista con todas las matrices
                sum_matrix += matrix_list[matrix_position][indice_fila][indice_columna]
                #guarda en la variable sum_matrix el valor del elemento de la matriz en la fila y columna de los indices
            lista_actual.append(sum_matrix)
            #print(lista_actual)
        matrix_actual.append(lista_actual)
        #print(matrix_actual)
    
    matrix_list.append(matrix_actual)
    #print(matrix_list)
    

    for matrix_fila in range(filas):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_fila != 1:
                print(f"{matrix_list[matrix_list_position][matrix_fila]}", end="   ")
            else:
                if matrix_list_position < len(matrix_list) - 2:
                    print(f"{matrix_list[matrix_list_position][matrix_fila]}", end=" + ")
                elif matrix_list_position < len(matrix_list) - 1:
                    print(f"{matrix_list[matrix_list_position][matrix_fila]}", end=" = ")
                else:
                    print(f"{matrix_list[matrix_list_position][matrix_fila]}", end="   ")
        print()
else:
    print("Deben ser un minimo de 2 matrices") 