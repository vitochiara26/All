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
        self.priorities = []
    
    def imprimir(self):
        if not self.start:
            return '[]'
                
        current_node = self.start
        cola_str = '['
        
        while current_node.after is not None :
            cola_str += (
                f" {current_node.value}(p:{current_node.priority}) <-"
            )
            current_node = current_node.after
        
        cola_str += f" {current_node.value}(p:{current_node.priority}) ]"
        return cola_str
    
    def enqueue_node(self, value, priority = 0):
        new_node = Node(value, priority)
        
        #verificar si ya existe la priority en priorities
        prio_index = -1
        for i in range(len(self.priorities)):
            if self.priorities[i][0] == priority:
                prio_index = i
                break
        
        if prio_index != -1:
            #Caso A: si existe la prioridad se inserta al final de su bloque de la misma prior
            indice_destino = self.priorities[prio_index][1] + 1
            self.__insert_at_index(new_node, indice_destino)
        
            for j in range(prio_index, len(self.priorities)):
                self.priorities[j][1] += 1
        
        else: 
            #caso B: una nueva prioridad
            insert_prio_pos = 0
            while (insert_prio_pos < len(self.priorities) and
            self.priorities[insert_prio_pos][0] > priority):
                insert_prio_pos += 1
            
            #determinar el indice de insercion
            if insert_prio_pos == 0:
                indice_destino = 0
            else:
                indice_destino = self.priorities[insert_prio_pos - 1][1] + 1
            
            self.__insert_at_index(new_node, indice_destino)
            
            self.priorities.insert(insert_prio_pos, [priority, indice_destino])
            
            # Desplazar el indice final de las prioridades menores
            for j in range(insert_prio_pos + 1, len(self.priorities)):
                self.priorities[j][1] += 1
                
        self.size += 1

    def __insert_at_index(self, node, index):
        if index == 0:
            node.after = self.start
            self.start = node
            if self.size == 0:
                self.end = node
            return
        
        current_node = self.start
        for _ in range(index - 1):
            current_node = current_node.after
        
        node.after = current_node.after
        current_node.after = node
        if node.after is None:
            self.end = node

    def dequeue_node(self):
        if not self.start:
            raise IndexError("La cola esta vacia.")
        
        node_to_dequeue = self.start
        self.start = self.start.after
        node_to_dequeue.after = None
        self.size -= 1
        
        if not self.start:
            self.end = None
            self.priorities = []
            return node_to_dequeue.value
        
        #desencolar indicie 0, de la cabeza
        for i in range(len(self.priorities)):
            self.priorities[i][1] -= 1
        
        if self.priorities[0][1] < 0:
            self.priorities.pop(0)
            
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
        


clientes = Cola()
clientes.enqueue_node("A")
clientes.enqueue_node("B")
clientes.enqueue_node("C")
clientes.enqueue_node("D")
clientes.enqueue_node("E")
clientes.enqueue_node("Z", 3)
clientes.enqueue_node("X", 1)
clientes.enqueue_node("Y", 2)


print(clientes.imprimir())
