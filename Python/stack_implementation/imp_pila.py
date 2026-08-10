class NodePila:
    def __init__(self, value):
        self.value = value
        self.down = None

class Pila:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push_node(self, value):
        new_node = NodePila(value)
        
        if not self.top:
            self.top = new_node
            self.size = 1
        else: 
            new_node.down = self.top
            self.top = new_node
            self.size += 1
    
    def pop_node(self):
        if not self.top:
            raise IndexError ('La pila esta vacia')
        else:
            node_to_pop = self.top
            self.top = node_to_pop.down
            node_to_pop.down = None
            self.size -= 1
        
        return node_to_pop.value
    
    def imprimir(self):
        if not self.top:
            return f'\\_ _/'
        
        pila_str = ''
        current_node = self.top
        
        while current_node.down:
            pila_str += f"\\_{current_node.value}_/\n"
            current_node = current_node.down
        
        pila_str += f"\\_{current_node.value}_/\n"
        return pila_str
            

# mi_pila = Pila()
# mi_pila.push_node('A')
# mi_pila.push_node('B')
# mi_pila.push_node('C')
# print(mi_pila.imprimir())

# mi_pila.pop_node()
# print(mi_pila.imprimir())

# mi_pila.pop_node()
# print(mi_pila.imprimir())

# print(mi_pila.pop_node())
# print(mi_pila.imprimir())

# print(mi_pila.pop_node())

