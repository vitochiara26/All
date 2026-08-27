class Node:
    def __init__(self, value, priority = 0):
        self.value = value
        self.priority = priority
        self.after = None

class Cola: 
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
    
    def imprimir(self):
        if not self.start:
            return '[]'
        
        current_node = self.start
        cola_str = '['
        if self.start.priority == self.end.priority:
            while current_node.after is not None :
                cola_str += f" {current_node.value} <-"
                current_node = current_node.after

            cola_str += f" {current_node.value} ]"
        else:
            while current_node.after is not None :
                cola_str += f" {current_node.value}(p:{current_node.priority}) <-"
                current_node = current_node.after

            cola_str += f" {current_node.value}(p:{current_node.priority}) ]"
            
        return cola_str
    
    def enqueue_node(self, value, priority = 0):
        new_node = Node(value, priority)
        
        #si la cola esta vacia
        if not self.start:
            self.start = new_node
            self.end = new_node
            self.size += 1
            return
        
        #si al prioridad del nuevo node es mayor a la prioridad del primer nodo en la cola
        if priority > self.start.priority:
            new_node.after = self.start
            self.start = new_node
            self.size += 1
            return
        
        #si al prioridad del nuevo node es igual o menor a la prioridad del ultimo nodo en la cola
        if priority <= self.end.priority:
            self.end.after = new_node
            self.end = new_node
            self.size += 1
            return
        
        # recorrer solo cuando la prioridad sea menor al del inicio pero mayor al ultimo de la cola
        current = self.start
        while current.after and current.after.priority >= priority:
            current = current.after

        # insertar el nuevo nodo en medio
        new_node.after = current.after
        current.after = new_node
        
        self.size += 1
    
    def dequeue_node(self):
        if not self.start:
            raise IndexError("La cola esta vacia.")
        
        node_to_dequeue = self.start
        self.start = self.start.after
        node_to_dequeue.after = None
        self.size -= 1
        
        return node_to_dequeue.value
    
    def front_node(self):
        if not self.start:
            raise IndexError("La cola esta vacia.")
        
        return self.start.value
    
    def reserve_cola(self):
        if self.size == 1:
            return
        
        current_node = self.dequeue_node()
        self.reserve_cola()
        self.enqueue_node(current_node)
        


# clientes = Cola()
# clientes.enqueue_node("A")
# clientes.enqueue_node("B")
# clientes.enqueue_node("C")
# clientes.enqueue_node("D")
# clientes.enqueue_node("E")


# print(clientes.imprimir())
# clientes.reserve_cola()
# print(clientes.imprimir())
# clientes.reserve_cola()
# print(clientes.imprimir())