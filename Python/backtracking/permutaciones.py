def generar_permutaciones(array):
    resultado = []
    
    def backtrack(camino_actual, opciones_restantes):
        if not opciones_restantes:
            resultado.append(camino_actual)
            return 

        for i in range(len(opciones_restantes)):
            eleccion = opciones_restantes[i]
            
            nuevas_opciones = opciones_restantes[:i] + opciones_restantes[i+1:]
            
            backtrack(camino_actual + [eleccion], nuevas_opciones)
    
    backtrack([], array)
    return resultado

def permutaciones_suma_par(array):
    suma_total = sum(x for x in array)
    if suma_total % 2 == 0:
        print(f'La suma del arreglo es: {suma_total} (Par). Generando permutaciones...')
        return generar_permutaciones(caracteres)
    else:
        print(f'La suma del arreglo es: {suma_total} (Impar). No hay permutaciones validas.')
        return []
        
    

caracteres = [1, 2, 4]
permutaciones = permutaciones_suma_par(caracteres)
for permutacion in permutaciones:
    print(permutacion)


