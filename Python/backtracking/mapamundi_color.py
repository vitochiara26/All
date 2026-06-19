import time
import os

# Definimos emojis para representar los enteros numéricos de los colores
# 0 = Sin color (⚪), 1 = Rojo (🔴), 2 = Azul (🔵), etc.
EMOJIS_COLOR = ["⚪", "🔴", "🔵", "🟢", "🟡", "🟣", "🟠"]
NOMBRES_PAISES = ["Argentina", "Uruguay", "Brasil", "Bolivia", "Perú"]

def obtener_vecinos(v, matriz):
    """Devuelve una lista con los nombres de los países limítrofes del país v."""
    vecinos = []
    for i in range(len(matriz)):
        if matriz[v][i] == 1:
            vecinos.append(NOMBRES_PAISES[i])
    return vecinos

def imprimir_pantalla(colores, matriz, pais_actual=None, accion="", tiempo=1):
    """Limpia la terminal y dibuja el estado actual del mapa y las decisiones."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("🌍 ALGORITMO DE COLORACIÓN DE MAPAMUNDI 🌍\n")
    print("-" * 50)
    
    # Imprimir los países y sus colores actuales
    for i in range(len(colores)):
        indicador = " <--- Evaluando" if i == pais_actual else ""
        print(f"País {NOMBRES_PAISES[i]}: {EMOJIS_COLOR[colores[i]]}{indicador}")
    
    print("-" * 50)
    
    # Imprimir información de contexto si estamos evaluando un país
    if pais_actual is not None:
        vecinos = obtener_vecinos(pais_actual, matriz)
        print(f"Fronteras de {NOMBRES_PAISES[pais_actual]}: {', '.join(vecinos)}")
    
    print(f"\nAcción: {accion}")
    time.sleep(tiempo)

def es_seguro(v, matriz, colores, color_prueba):
    """Verifica si el color_prueba es válido para el país v."""
    for i in range(len(matriz)):
        # Si son limítrofes (matriz == 1) y el vecino ya tiene ese color, no es seguro
        if matriz[v][i] == 1 and colores[i] == color_prueba:
            return False
    return True

def colorear_backtracking(matriz, max_colores, colores, v):
    """Algoritmo recursivo para probar combinaciones de colores."""
    N = len(matriz)
    
    # Caso base: Si todos los países han sido coloreados
    if v == N:
        return True
    
    # Intentar asignar colores desde el 1 hasta max_colores
    for c in range(1, max_colores + 1):
        imprimir_pantalla(colores, matriz, v, f"Probando color {EMOJIS_COLOR[c]} en País {NOMBRES_PAISES[v]}")
        
        if es_seguro(v, matriz, colores, c):
            colores[v] = c  # Asignamos el color
            imprimir_pantalla(colores, matriz, v, f"✅ ¡{EMOJIS_COLOR[c]} asignado a País {NOMBRES_PAISES[v]}!")
            
            # Recursión: intentar colorear el resto de los países
            if colorear_backtracking(matriz, max_colores, colores, v + 1):
                return True
            
            # BACKTRACKING: Si la llamada recursiva devolvió False, este camino no sirve.
            # Quitamos el color (volvemos a 0) y probamos con el siguiente 'c'.
            colores[v] = 0
            imprimir_pantalla(colores, matriz, v, f"🔙 BACKTRACKING: El camino falló. Borrando color de {NOMBRES_PAISES[v]}.")
        else:
            imprimir_pantalla(colores, matriz, v, f"❌ Conflicto: {EMOJIS_COLOR[c]} choca con un país limítrofe.")
            
    return False

def resolver_mapa(matriz):
    N = len(matriz)
    # Bucle iterativo para encontrar el MÍNIMO de colores posibles
    for max_colores in range(1, N + 1):
        colores = [0] * N # Inicializamos todos los países con color 0 (⚪)
        
        imprimir_pantalla(colores, matriz, None, f"🔄 INTENTANDO RESOLVER EL MAPA CON {max_colores} COLOR(ES)...", tiempo=2)
        
        if colorear_backtracking(matriz, max_colores, colores, 0):
            imprimir_pantalla(colores, matriz, None, f"🎉 ¡ÉXITO! El mapa requiere un mínimo de {max_colores} colores.", tiempo=0)
            return True
            
    return False

# ==========================================
# CONFIGURACIÓN DEL MAPA (MATRIZ LÓGICA NxN)
# ==========================================
# Supongamos un mapa de 5 países Argentina, Uruguay, Brasil, Bolivia, Perú.
# 1 = Son limítrofes | 0 = No son limítrofes o es el mismo país
matriz_adyacencia = [
    # A  B  C  D  E
    [0, 1, 1, 1, 0], # A limita con B, C, D
    [1, 0, 1, 0, 0], # B limita con A, C
    [1, 1, 0, 1, 1], # C limita con A, B, D, E
    [1, 0, 1, 0, 1], # D limita con A, C, E
    [0, 0, 1, 1, 0]  # E limita con C, D
]

# Ejecución del programa
resolver_mapa(matriz_adyacencia)
