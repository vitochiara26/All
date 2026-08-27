import queue_imp as que

def eliminar__negativos(cola_enteros):
    tamaño_inicial = cola_enteros.size
    
    while tamaño_inicial > 0:
        entero = cola_enteros.dequeue_node()
        if entero >= 0:
            cola_enteros.enqueue_node(entero)
        tamaño_inicial -= 1
    
    return cola_enteros

cola_enteros = que.Cola()
cola_enteros.enqueue_node(65)
cola_enteros.enqueue_node(-2)
cola_enteros.enqueue_node(7)
cola_enteros.enqueue_node(-38)
cola_enteros.enqueue_node(-93)
cola_enteros.enqueue_node(23)
cola_enteros.enqueue_node(-83)
cola_enteros.enqueue_node(25)
cola_enteros.enqueue_node(-7)
cola_enteros.enqueue_node(34)

print(cola_enteros.imprimir())

cola_enteros = eliminar__negativos(cola_enteros)

print(cola_enteros.imprimir())

