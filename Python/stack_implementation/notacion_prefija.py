import sys
import os

carpeta_atual = os.path.dirname(os.path.abspath(__file__))
carpeta_padre = os.path.dirname(carpeta_atual)
sys.path.append(carpeta_padre)

import list_implementation.implementacion_lista as lis
import imp_pila as pil

def Operador(E) -> bool:
    """Verificar si el token es un operador"""
    return str(E) in ("+", "-", "*", "/")

def evaluar_operacion(op, op1, op2):
    """Aplica la operacion"""
    match op:
        case "+":
            return op1 + op2
        case "-":
            return op1 - op2
        case "*":
            return op1 * op2
        case "/":
            return op1 / op2
        case _:
            raise ValueError(f"Operador desconocido: {op}")

def evaluar_prefija(expresion_prefija):
    """Evalua una expresion prefija representada en una Lista.
    Recorre la expresion de DER a IZQ usando una Pila auxiliar"""
    pila_eval = pil.Pila()
    
    for i in range(expresion_prefija.size -1, -1, -1):
        token = expresion_prefija.search_node_value(i)
        
        #si es operador, extrae 2 operando, opera y reapila el resultado
        if Operador(token):
            op1 = pila_eval.pop_node()
            op2 = pila_eval.pop_node()
            resultado = evaluar_operacion(token, op1, op2)
            pila_eval.push_node(resultado)
        #si es operando, apilar directamente 
        else:
            pila_eval.push_node(float(token))
    
    return pila_eval.pop_node()


expresion_ejemplo = lis.Lista()
expresion_ejemplo.insert_node("*")
expresion_ejemplo.insert_node("+")
expresion_ejemplo.insert_node("10")
expresion_ejemplo.insert_node("2")
expresion_ejemplo.insert_node("5")

resultado = evaluar_prefija(expresion_ejemplo)
print("Expresion prefija:", expresion_ejemplo.imprimir())
print("Resultado de la evalucion:", resultado)
