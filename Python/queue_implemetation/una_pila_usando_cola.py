import sys
import os

carpeta_atual = os.path.dirname(os.path.abspath(__file__))
carpeta_padre = os.path.dirname(carpeta_atual)
sys.path.append(carpeta_padre)

import stack_implementation.imp_pila as pil
import queue_imp as que

def push(cola, value):
    cola.enqueue_node(value)
    for _ in range(cola.size - 1):
        cola.enqueue_node(cola.dequeue_node())

def pop(cola):
    return cola.dequeue_node()

def sumar_pila_que_en_realidad_es_cola(cola):
    suma = 0
    while cola.size > 0:
        val = pop(cola)
        suma += val
    return suma

mi_pila_usando_cola = que.Cola()
push(mi_pila_usando_cola, 10)
print(mi_pila_usando_cola.imprimir())
push(mi_pila_usando_cola, 20)
print(mi_pila_usando_cola.imprimir())
push(mi_pila_usando_cola, 30)
print(mi_pila_usando_cola.imprimir())
push(mi_pila_usando_cola, 40)
print(mi_pila_usando_cola.imprimir())
pop(mi_pila_usando_cola)
print(mi_pila_usando_cola.imprimir())

print("Suma total: ", sumar_pila_que_en_realidad_es_cola(mi_pila_usando_cola))


