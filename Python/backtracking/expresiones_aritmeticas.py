def combinar_operaciones(numeros, respuesta, combinacion, operadores, numero_actual = 1):
        if numero_actual > numeros:
            resultado = operar_combinacion(combinacion)
            if resultado == respuesta:
                return f'La combinacion de operadores {combinacion} da como resultado {resultado}'
            return 
        
        for operador in operadores:
            combinacion.extend([operador, numero_actual])
            resultado = combinar_operaciones(numeros, respuesta, combinacion, operadores, numero_actual + 1)
            
            if resultado:
                return resultado
            
            combinacion.pop()
            combinacion.pop()


def operar_combinacion(combinacion, resultado = 0, operando = 0, digito = 1):
    if operando < len(combinacion):
        match combinacion[operando]:
            case "+":
                resultado += combinacion[digito]
                operando += 2
                digito += 2
                return operar_combinacion(combinacion, resultado, operando, digito)
            case "-":
                resultado -= combinacion[digito]
                operando += 2
                digito += 2
                return operar_combinacion(combinacion, resultado, operando, digito)

            case "*":
                resultado *= combinacion[digito]
                operando += 2
                digito += 2
                return operar_combinacion(combinacion, resultado, operando, digito)

            case "/":
                resultado /= combinacion[digito]
                operando += 2
                digito += 2
                return operar_combinacion(combinacion, resultado, operando, digito)
                
    else:
        return resultado


operadores = ['+', '-', '*', '/']
combinacion = []

print(combinar_operaciones(4, 0, combinacion, operadores))
