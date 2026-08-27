import queue_imp as queue


def mayor_y_menor_elemento(cola, mayor = None, menor = None):
    if cola.size == 0:
            return mayor, menor
    
    current_node = cola.dequeue_node()
    if mayor is None and menor is None:
        mayor = menor = current_node
    
    if mayor < current_node:
        mayor = current_node
    if menor > current_node:
        menor = current_node
    
    mayor_elem, menor_elem = mayor_y_menor_elemento(cola, mayor, menor)
    cola.enqueue_node(current_node)
    return mayor_elem, menor_elem


colita = queue.Cola()
colita.enqueue_node(8)
colita.enqueue_node(2)
colita.enqueue_node(22)
colita.enqueue_node(37)
colita.enqueue_node(64)
colita.enqueue_node(4)
colita.enqueue_node(14)
colita.enqueue_node(57)
colita.enqueue_node(5)

mayor_elem, menor_elem = mayor_y_menor_elemento(colita)
print("Cola: ", colita.imprimir())
print("Mayor ", mayor_elem)
print("Menor ", menor_elem)