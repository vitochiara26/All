import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stack_implementation.imp_pila as pil
import queue_imp as que


def contar_frecuencia_a_pila(cola_origen):
    if cola_origen.size == 0:
        raise IndexError("La cola está vacia.")

    frecuencias = {}
    orden_aparicion = []
    
    #1. Recorrer la cola y contar las frecuencias
    tamaño_inicial = cola_origen.size
    for _ in range(tamaño_inicial):
        elem = cola_origen.dequeue_node()
        
        if elem not in frecuencias:
            frecuencias[elem] = 0
            orden_aparicion.append(elem)
        frecuencias[elem] += 1
        
        #Re-encolar para ir girando y preservando al cola
        cola_origen.enqueue_node(elem)
    
    #2. Generar pila resultado
    pila_resultado = pil.Pila()
    
    for elem in orden_aparicion:
        cant = frecuencias[elem]
        
        #apilamos el elemento encontrado y luego la cantidad de ocurrencias
        pila_resultado.push_node(elem)
        pila_resultado.push_node(cant)
    
    return pila_resultado


cola_datos = que.Cola()

for num in [2, 5, 2, 3, 5, 2]:
    cola_datos.enqueue_node(num)

print("Cola original:", cola_datos.imprimir())

pila_frecuencias = contar_frecuencia_a_pila(cola_datos)

print(f"\nPila resultado (Tope arriba):")
print(pila_frecuencias.imprimir())

print("\nCola original intacta:", cola_datos.imprimir())
