from time import sleep
import os 

def imprimir_laberinto(laberinto, path):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for fila in range(len(laberinto)):
        linea = ""
        for columna in range(len(laberinto)):
            if (fila, columna) in path:
                linea += "🟩 "
            elif laberinto[fila][columna] == 1:
                linea += "🧱 "
            else:
                linea += "   "
        print(linea)
    print("\nBuscando salida...")


def resolver_laberinto_backtracking(laberinto, fil, col, visited, path):
    N = len(laberinto)
    #caso base, si llego a la salida
    if fil == N -1 and col == N -1:
        path.append((fil, col))
        imprimir_laberinto(laberinto, path)
        print("\nSalida encontrada!!!")
        return True
    
    #verificar transitabilidad
    if 0 <= fil < N and 0 <= col < N and laberinto[fil][col] == 0 and (fil, col) not in visited:
        visited.add((fil,col))
        path.append((fil,col))
        
        imprimir_laberinto(laberinto, path)
        sleep(0.2)
        
        for dir_fil, dir_col in [(-1,0),(0,1),(1,0),(0,-1)]:
            if resolver_laberinto_backtracking(laberinto, fil + dir_fil, col + dir_col, visited, path):
                return True
            
        path.pop()
        visited.remove((fil, col))
        imprimir_laberinto(laberinto, path)
        sleep(0.2)
        
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
