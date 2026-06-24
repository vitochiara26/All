from time import sleep #se importa time para usar sleep para detener el frame de impresion
import os #se importa os para limpiar la terminal al hacer una impresion nueva

def imprimir_laberinto(laberinto, path):
    '''funcion que va a leer el laberinto en un paso actual y mostrar su estado en terminal'''
    os.system('cls' if os.name == 'nt' else 'clear') #borra lo existente en terminal
    
    
    for fila in range(len(laberinto)):
        #itera cada fila del laberinto 
        linea = "" #se usara para guarda los estados de cada celda de la matriz del laberinto
        for columna in range(len(laberinto)):
            #itera cada columna de cada fila
            if (fila, columna) in path:
                #si la tupla creada por el valor de la fila y la columna actual se encuentran en...
                #path (que es una lista donde se guardan las tuplas de fila y columna por donde... 
                # ya pasamos) la pinta de verde porque o estamos parados ahi o ya pasamos por ahi
                linea += "🟩 "
            elif laberinto[fila][columna] == 1:
                #si el valor en esa celda es 1, significa que no se puede transitar por ahi
                linea += "🧱 "
            else:
                #no es ninguna de las anteriores, es un 0, lo que significa que es transitable...
                #lo dibujamos como un espacio vacio
                linea += "   "
        print(linea)
    print("\nBuscando salida...")


def resolver_laberinto_backtracking(laberinto, fil, col, visited, path):
    ''''Funcio que empieza a avanzar por el laberinto hasta buscar la salida, toma el laberinto
    creado por unos y ceros, un valor de fila y un valor de columna, que indica a partir de donde 
    comenzamos en el laberinto, toma un conjunto (visited) donde se guardan tuplas de las celdas 
    con valor fila, columna que ya visitamos, y una lista (path) de tuplas que es el historial o 
    rastro que venimos recorriendo'''
    
    N = len(laberinto) #se declara la dimension del laberinto como N
    #caso base, si llego a la salida, la salida se declara como la celda en la fila final y la...
    #columna final
    if fil == N -1 and col == N -1:
        #se agrega a la lista de camino recorrido el paso dado
        path.append((fil, col))
        imprimir_laberinto(laberinto, path)
        print("\nSalida encontrada!!!")
        return True
    
    #verificar transitabilidad
    #si la fila y la columna esta entre 0 y N-1 y el ese celda es transitable (que tenga valor 0)...
    #y que esa celda no se haya visitado antes (se verifica para evitar caer en un bucle)
    if 0 <= fil < N and 0 <= col < N and laberinto[fil][col] == 0 and (fil, col) not in visited:
        visited.add((fil,col)) #se agrega la celda como visitada
        path.append((fil,col)) #se agrega la celda al cammino trazado
        
        imprimir_laberinto(laberinto, path)
        sleep(0.2)
        
        # se itera sobre los 4 movimientos disponibles en sentido horario:
        #arriba (-1,0) restamos 1 a la fila 
        #derecha (0,1) sumamos 1 a la columna
        #abajo (1,0) sumamos 1 a la fila
        #izquierda (0,-1) restamos 1 a la columna
        #se realiza un desempaquetado de tupla, se le asigna el valor en el indice 0 de la tupla...
        # a dir_fil y se le asigna el valor en el indice 1 de la tupla a dir_col 
        for dir_fil, dir_col in [(-1,0),(0,1),(1,0),(0,-1)]:
            #se llama a la recursion la funcion (que no hace nada si ese movimiento no es posible...
            #si se choca con una pared o una celda ya visitada), sumado al parametro de fila y de...
            #columna lo que indique la tupla de movimiento, los demas parametros se pasan como...
            #han venido actualizandose
            if resolver_laberinto_backtracking(laberinto, fil+dir_fil,col+dir_col, visited, path):
                #la funcion anterior regresa True si se llego al destino, regresa False si al...
                #iterar todo el for anterior no cunple ningun movimiento con la verificacion de...
                #transitabilidad
                return True
        
        #si no sucede el Return de arriba, se elimina del camino recorrido y de las celdas...
        # visitadas la ultima celda agregada 
        path.pop()
        visited.remove((fil, col))
        imprimir_laberinto(laberinto, path)
        sleep(0.2)
        #se regresa false ya que partir de esa posicion de se puede avanzar 
        return False


laberinto = [   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
                [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],
                [1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1],
                [1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
                [1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
                [1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1],
                [1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
                [1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
                [1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1],
                [1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1],
                [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
                [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
                [1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
                [1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1],
                [1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1],
                [1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1],
                [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            ]

solution_path = []
visiteds = set()
resolver_laberinto_backtracking(laberinto, 1, 1, visiteds, solution_path)
