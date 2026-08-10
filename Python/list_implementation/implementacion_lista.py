class Node:
    def __init__(self, value):
        self.value = value
        self.to_right = None
        self.to_left = None
    
class NodeSencillo:
    def __init__(self, value):
        self.value = value
        self.to_right = None

class Lista:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_node(self, value, index = None):
        new_node = Node(value)
        
        #si la lista esta vacia
        if self.head == None:
            self.head  = new_node
            self.size = 1
            return 
        
        #normalizacion del indice si pasan uno negativo
        if index != None and index < 0:
            index = self.size + index
            if index < 0:
                index = 0
        
        #si el indice de insercion dado es 0
        if index == 0:
            new_node.to_right = self.head
            self.head.to_left = new_node
            self.head = new_node
            self.size += 1
            return
        
        contador = 0
        current_node = self.head
        while not current_node.to_right is None and (index is None or contador < index):
            contador += 1
            current_node = current_node.to_right
        
        # Insertar al final
        if (index is None or contador < index):
            current_node.to_right = new_node    
            new_node.to_left = current_node
            self.size += 1
            return
        else: #insercion intermedia 
            new_node.to_right = current_node
            new_node.to_left = current_node.to_left
            current_node.to_left.to_right = new_node
            current_node.to_left = new_node
            self.size += 1
            return

    def imprimir(self):
        if self.head is None:
            return '[]'
        
        contador = 0
        current_node = self.head
        lista_str = '[' 
        
        while current_node.to_right != None :
            lista_str += f'{current_node.value}, '
            contador += 1
            current_node = current_node.to_right
        
        lista_str += f'{current_node.value}'
        lista_str += ']' 
        
        return lista_str
    
    def search_node(self, index):
        if index < 0:
            index = self.size + index
            
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        
        current_node = self.head
        for pos in range(self.size):
            if pos == index:
                return f'[{current_node.value}]'
            current_node = current_node.to_right
        
    def search_node_value(self, index):
        if index < 0:
            index = self.size + index
            
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        
        current_node = self.head
        for pos in range(self.size):
            if pos == index:
                return current_node.value
            current_node = current_node.to_right

    def remove_node_by_occurrence(self, value):
        current_node = self.head
        for pos in range(self.size):
            if current_node.value == value:
                if pos == 0:
                    self.head = current_node.to_right
                    self.head.to_left = None
                    current_node.to_right = None
                    self.size -= 1
                    return
                
                if pos == self.size - 1:
                    current_node.to_left.to_right = None
                    current_node.to_left = None
                    self.size -= 1
                    return
                
                current_node.to_left.to_right = current_node.to_right
                current_node.to_right.to_left = current_node.to_left
                current_node.to_left = None
                current_node.to_right = None
                self.size -= 1
                return
            else :
                current_node = current_node.to_right
        raise ValueError ('list.remove(x): x not in list')
    
    def remove_node_by_index(self, index):
        if index < 0:
            index = self.size + index
        
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        
        current_node = self.head
        for pos in range(self.size):
            if pos == index:
                if pos == 0:
                    self.head = current_node.to_right
                    self.head.to_left = None
                    current_node.to_right = None
                    self.size -= 1
                    return
                
                if pos == self.size - 1:
                    current_node.to_left.to_right = None
                    current_node.to_left = None
                    self.size -= 1
                    return
                
                current_node.to_left.to_right = current_node.to_right
                current_node.to_right.to_left = current_node.to_left
                current_node.to_left = None
                current_node.to_right = None
                self.size -= 1
                return
            else :
                current_node = current_node.to_right

    def pop_node_by_index(self):
        if index < 0:
            index = self.size + index
            
            if index < 0 or index >= self.size:
                raise IndexError("list index out of range")
            
            current_node = self.head
            for pos in range(self.size):
                if pos == index:
                    if pos == 0:
                        self.head = current_node.to_right
                        self.head.to_left = None
                        current_node.to_right = None
                        self.size -= 1
                        return current_node.value
                    
                    if pos == self.size - 1:
                        current_node.to_left.to_right = None
                        current_node.to_left = None
                        self.size -= 1
                        return current_node.value
                    
                    current_node.to_left.to_right = current_node.to_right
                    current_node.to_right.to_left = current_node.to_left
                    current_node.to_left = None
                    current_node.to_right = None
                    self.size -= 1
                    return current_node.value
                else :
                    current_node = current_node.to_right
    
    def replace_value_of_node(self, value, index):
        if index < 0:
            index = self.size + index
            
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")
        
        current_node = self.head
        for pos in range(self.size):
            if pos == index:
                current_node.value = value
                return
            current_node = current_node.to_right
    
    #def segment_list(self, start = 0, end = None, step = 1):
    def segment_list(self, arg1 = None, arg2 = None, step = 1):
        #step no puede ser 0
        if step == 0:
            raise ValueError("slice step cannot be zero")
        
        #asignar pase de argumentos dependiendo de la cantidad que se envien 
        if arg1 is None and arg2 is None:
            start = self.size - 1 if step < 0 else 0
            end = -1 if step < 0 else self.size
        elif arg2 is None:
            start = 0 if step > 0 else self.size - 1
            end = arg1
        else:
            start = arg1
            end = arg2
        
        #normalizacion de indices
        if start < 0:
            start = max(-1 if step < 0 else 0, self.size + start)
        if end < 0 and (arg1 is not None or arg2 is not None):
            end = max(-1 if step < 0 else 0, self.size + end)
        
        #ajuste de los limites del rango de la lista
        if step > 0:
            start = min(self.size, max(0, start))
            end = min(self.size, max(0, end))
        else: # step < 0
            start = min(self.size - 1, max(-1, start))
            end = min(self.size - 1, max(-1, end))
        
        #con mi misma clase creo una nueva lista
        new_list = Lista()
        
        #si la cabeza esta vacia, si el tamaño es cero,
        if self.head is None or self.size == 0:
            return new_list
        
        #buscamos el indice para iniciar
        current_node = self.head
        contador = 0
        while current_node != None and contador < start:
            current_node = current_node.to_right
            contador += 1
        
        if current_node is None:
            return new_list
        
        #si el salto es positivo
        if step > 0:
            while current_node != None and contador < end:
                new_list.insert_node(current_node.value)
                #dar los saltos
                pasos = 0
                while current_node != None and pasos < step:
                    current_node = current_node.to_right
                    pasos += 1
                contador += step
        
        #si el salto es negativo
        else:
            while current_node != None and contador > end:
                new_list.insert_node(current_node.value)
                #dar los saltos
                pasos = 0
                while current_node != None and pasos < abs(step):
                    current_node = current_node.to_left
                    pasos += 1
                contador += step
        
        return new_list

class ListaCircular:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_node(self, value, index = None):
        new_node = Node(value)
        
        #si la lista esta vacia
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.to_right = new_node
            new_node.to_left = new_node
            self.size = 1
            return 
        
        #normalizacion del indice si pasan uno negativo
        if index != None and index < 0:
            index = self.size + index
            if index < 0:
                index = 0
        
        #si el indice de insercion dado es 0
        if index == 0:
            new_node.to_right = self.head
            new_node.to_left = self.tail
            self.head.to_left = new_node
            self.tail.to_right = new_node
            self.head = new_node
            self.size += 1
            return
        
        # Insertar al final
        if index is None or index == self.size:
            new_node.to_left = self.tail
            new_node.to_right = self.head
            self.tail.to_right = new_node
            self.head.to_left = new_node
            self.tail = new_node
            self.size += 1
            return
        
        contador = 0
        current_node = self.head
        while contador < index:
            contador += 1
            current_node = current_node.to_right
        
        new_node.to_right = current_node
        new_node.to_left = current_node.to_left
        current_node.to_left.to_right = new_node
        current_node.to_left = new_node
        self.size += 1
        return
    
    def imprimir(self):
        if self.head is None:
            return '[]'
        
        contador = 0
        current_node = self.head
        lista_str = '[' 
        
        while contador < self.size - 1 :
            lista_str += f'{current_node.value}, '
            contador += 1
            current_node = current_node.to_right
            
        
        lista_str += f'{current_node.value}'
        lista_str += ']' 
        
        return lista_str

class ListaSencilla:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_node(self, value, index = None):
        new_node = NodeSencillo(value)
        
        #si la lista esta vacia
        if self.head == None:
            self.head  = new_node
            self.size = 1
            return 
        
        #normalizacion del indice si pasan uno negativo
        if index != None and index < 0:
            index = self.size + index
            if index < 0:
                index = 0
        
        #si el indice de insercion dado es 0
        if index == 0:
            new_node.to_right = self.head
            self.head = new_node
            self.size += 1
            return
        
        # Insertar al final
        if (index is None or index == self.size - 1):
            current_node = self.head
            while not current_node.to_right is None:
                current_node = current_node.to_right
            
            current_node.to_right = new_node    
            self.size += 1
            return

        #insercion intermedia
        contador = 0
        current_node = self.head
        while contador < index - 1:
            contador += 1
            current_node = current_node.to_right
        
        new_node.to_right = current_node.to_right
        current_node.to_right = new_node
        self.size += 1
        return
    
    def remove_node_by_index(self, index = None):
        if index < 0:
            index = self.size + index
        
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")

        if index == 0:
            a_eliminar = self.head
            self.head = a_eliminar.to_right
            a_eliminar.to_right = None
            self.size -= 1
            return
        
        if index == self.size - 1:
            contador = 0
            current_node = self.head
            while contador < index - 1:
                contador += 1
                current_node = current_node.to_right
            a_eliminar = current_node.to_right
            current_node.to_right = None 
            a_eliminar.to_right = None
            self.size -= 1
            return
        
        contador = 0
        current_node = self.head
        while contador < index - 1:
            contador += 1
            current_node = current_node.to_right
        a_eliminar = current_node.to_right
        current_node.to_right = a_eliminar.to_right
        a_eliminar.to_right = None
        self.size -= 1
        return
    
    def search_node(self, index):
            if index < 0:
                index = self.size + index
                
            if index < 0 or index >= self.size:
                raise IndexError("list index out of range")
            
            current_node = self.head
            for pos in range(self.size):
                if pos == index:
                    return current_node.value
                current_node = current_node.to_right
    
    def imprimir(self):
        if self.head is None:
            return '[]'
        
        contador = 0
        current_node = self.head
        lista_str = '[' 
        
        while current_node.to_right != None :
            lista_str += f'{current_node.value}, '
            contador += 1
            current_node = current_node.to_right
        
        lista_str += f'{current_node.value}'
        lista_str += ']' 
        
        return lista_str
    
    

# mi_lista = Lista()
# mi_lista.insert_node('A')
# mi_lista.insert_node('B', 0)
# mi_lista.insert_node('C')
# mi_lista.insert_node('D', 2)
# mi_lista.insert_node('E')
# mi_lista.insert_node('F')

# print(mi_lista.imprimir())

# print(mi_lista.search_node(3))
# mi_lista.remove_node_by_occurrence('C')
# print(mi_lista.imprimir())

# mi_lista.remove_node_by_index(-1)
#  print(mi_lista.imprimir())

#  mi_lista.replace_value_of_node('Z', 1)
# print(mi_lista.imprimir())

# second_list = mi_lista.segment_list(step=-1)
# print(second_list.imprimir())

# mi_lista = ListaCircular()
# mi_lista.insert_node('A')
# mi_lista.insert_node('B', 0)
# mi_lista.insert_node('C', 0)
# mi_lista.insert_node('D', 0)
# mi_lista.insert_node('E', 0)
# mi_lista.insert_node('F', 0)
# mi_lista.insert_node('X')
# mi_lista.insert_node('Y')
# mi_lista.insert_node('Z')
# mi_lista.insert_node('Ñ', 5)

# print(mi_lista.imprimir())

# mi_lista = ListaSencilla()
# mi_lista.insert_node('A')
# print(mi_lista.imprimir())

# mi_lista.insert_node('B', 0)
# print(mi_lista.imprimir())

# mi_lista.insert_node('C', 0)
# print(mi_lista.imprimir())

# mi_lista.insert_node('D', 0)
# print(mi_lista.imprimir())

# mi_lista.insert_node('Z')
# print(mi_lista.imprimir())

# mi_lista.insert_node('Y', 4)
# print(mi_lista.imprimir())

# print(mi_lista.search_node(3))
