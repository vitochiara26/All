def obtener_numeros(m):
    # Se valida que m no se mayor a 9 ni menor a 1
    if not (1 <= m <= 9):
        return []

    resultados = []
    
    def crear_numero(numero_actual, digitos_usados, n):
        #n = longitud actual, si n alcanza a m llegamos al limite
        if n == m:
            resultados.append(numero_actual) #guardamos ese numero creado
            return #return para salir del backtracking
        
        #exploramos cada digito 1 a 1 desde 1 hasta 9
        for digito in range(1,10):
            #Cada digito nuevo a usar debe ser distinto de uno usado anteriormente
            if digito not in digitos_usados:
                #formamos la cifra usando ese digito 
                cifra = numero_actual * 10 + digito

                #una cifra de longitud n+1 debe ser multiplo de n+1
                if cifra % (n +1) == 0:
                    #se registra el digito que se esta usando como ya usado
                    digitos_usados.add(digito)

                    #bajamos un nivel recursivo para evaluar el siguiente digito
                    crear_numero(cifra, digitos_usados, n + 1)

                    #se deshace el backtracking para explorar otra combinacion
                    digitos_usados.remove(digito)

    #inicio de  recursion, numero_actual = 0, digitos_usados como un conjunto vacio, y longitud actual de la cifra en 0 (n)
    crear_numero(0, set(), 0)
    
    return resultados


m = 3
numeros_validos = obtener_numeros(m)
print(f"Se encontraron {len(numeros_validos)} numeros validos para m = {m}:")
print(numeros_validos)