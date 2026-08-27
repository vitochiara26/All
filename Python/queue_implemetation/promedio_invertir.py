import queue_imp as queue


def promedio_y_reverse(cola, suma = 0, elementos = None):
        if elementos is None:
            elementos = cola.size
    
        if cola.size == 0:
            return 0 if elementos == 0 else suma / elementos
        
        current_node = cola.dequeue_node()
        suma += current_node
        promedio = promedio_y_reverse(cola, suma, elementos)
        
        cola.enqueue_node(current_node)
        return promedio


colita = queue.Cola()
colita.enqueue_node(1)
colita.enqueue_node(2)
colita.enqueue_node(3)
colita.enqueue_node(4)
colita.enqueue_node(5)

print("Cola original:  ", colita.imprimir())
promedio = promedio_y_reverse(colita)

print("Promedio:       ", promedio)
print("Cola invertida: ", colita.imprimir())