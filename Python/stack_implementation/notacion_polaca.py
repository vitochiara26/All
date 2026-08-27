import sys
import os

carpeta_atual = os.path.dirname(os.path.abspath(__file__))
carpeta_padre = os.path.dirname(carpeta_atual)
sys.path.append(carpeta_padre)

import list_implementation.implementacion_lista as lis
import imp_pila as pil


def precedencia(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infija_a_polaca(lista_infija):
    pila_operadores = pil.Pila() #para operadores 
    resultado_tokens = lis.Lista() #para ir constuyendo el resultado invertido
    
    #1. Recorrer lista infija de Der a Izq
    for i in range(lista_infija.size -1, -1, -1):
        token = lista_infija.search_node_value(i)
        
        if str(token).isalnum(): #si es operando (var o num)
            resultado_tokens.insert_node(token)
            
        elif token == ')': #Al ir en reversa ')' actua como apertura en lugar de cierre
            pila_operadores.push_node(token)
            
        elif token == '(': # '(' actua como cierre, desapila hasta encontrar ')'
            while pila_operadores.top and pila_operadores.top.value != ')':
                resultado_tokens.insert_node(pila_operadores.pop_node())
            if pila_operadores.top:
                pila_operadores.pop_node() #se descarta el ')'
        
        else: #si es un operador
            while ( pila_operadores.top and
                    pila_operadores.top.value != ')' and
                    precedencia(pila_operadores.top.value) > precedencia(token)):
                resultado_tokens.insert_node(pila_operadores.pop_node())
            pila_operadores.push_node(token)
    
    #vaciar el resto de operadores 
    while pila_operadores.top:
        resultado_tokens.insert_node(pila_operadores.pop_node())
    
    #2. Guardar en la pila Final
    #al recorrer una lista el primer token quedara en la cima de la pila
    pila_polaca = pil.Pila()
    for i in range(0, resultado_tokens.size):
        pila_polaca.push_node(resultado_tokens.search_node_value(i))

    return pila_polaca

def evaluar_operacion(op, op1, op2):
    match op:
        case '+':
            return op1 + op2
        case '-':
            return op1 - op2
        case '*':
            return op1 * op2
        case '/':
            return op1 / op2
        case '^':
            return op1 ** op2
        case _:
            raise ValueError(f"Operador desconocido: {op}")

def evaluar_pila_polaca(pila_polaca):
    pila_eval = pil.Pila()
    
    #Procesar la pila hasta que quede vacia
    while pila_polaca.top:
        token = pila_polaca.pop_node()
        
        #convertir a valor numerico 
        if isinstance(token, (int, float)) or str(token).replace('.', '', 1).isdigit():
            pila_eval.push_node(float(token))
        else:
            #si es operador apilar en la estructura de evaluacion
            pila_eval.push_node(token)
        
        #intentar reducir si en la cima de pila_eval hay: [num2, num1, op]
        mientras_sea_reducible = True
        while mientras_sea_reducible and pila_eval.size >= 3:
            val2 = pila_eval.top.value
            val1 = pila_eval.top.down.value
            op = pila_eval.top.down.down.value
            
            #verificar si tenemos la secuencia (op, num1, num2)
            if (isinstance(val2, (int, float)) and
                isinstance(val1, (int, float)) and
                isinstance(op, str) and
                op in "+-*/^"):
                
                #desapilar los elementos 
                pila_eval.pop_node()
                pila_eval.pop_node()
                pila_eval.pop_node()
                
                #calular resultado y apilarlo
                res = evaluar_operacion(op, val1, val2)
                pila_eval.push_node(res)
            else:
                mientras_sea_reducible = False
        
    return pila_eval.pop_node()


expresion = lis.Lista()
expresion.insert_node('(')
expresion.insert_node('3')
expresion.insert_node('+')
expresion.insert_node('(')
expresion.insert_node('8')
expresion.insert_node('/')
expresion.insert_node('2')
expresion.insert_node(')')
expresion.insert_node(')')

print("Expresion Infija Original:", expresion.imprimir())

pila_polaca = infija_a_polaca(expresion)
print("\nPila en Notacion Polaca")
print(pila_polaca.imprimir())

resultado = evaluar_pila_polaca(pila_polaca)
print("Resultado de la evaluacion:", resultado)