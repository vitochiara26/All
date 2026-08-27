import sys
import os

carpeta_atual = os.path.dirname(os.path.abspath(__file__))
carpeta_padre = os.path.dirname(carpeta_atual)
sys.path.append(carpeta_padre)

import stack_implementation.imp_pila as pil
import queue_imp as que

def enqueue(pila_in, value):
    pila_in.push_node(value)

def dequeue(pila_in, pila_out):
    if pila_out.size == 0:
        while pila_in.size > 0:
            pila_out.push_node(pila_in.pop_node())
    
    if pila_out.size == 0:
        raise IndexError("La pila está vacia.")
    
    return pila_out.pop_node()

def sumar_cola_que_en_realidad_es_pila(pila_in, pila_out):
    suma = 0
    while pila_out.size > 0:
        val = dequeue(pila_in, pila_out)
        suma += val
    return suma

pila_entries = pil.Pila()
pila_exits = pil.Pila()

enqueue(pila_entries, 10)
enqueue(pila_entries, 20)
enqueue(pila_entries, 30)

dequeue(pila_entries, pila_exits)

print(sumar_cola_que_en_realidad_es_pila(pila_entries, pila_exits))
