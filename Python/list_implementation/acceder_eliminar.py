import implementacion_lista as my_li

def acceder_a_nodo(index, lista):
    if index < 0:
            index = lista.size + index
            
    if index < 0 or index >= lista.size:
        raise IndexError("list index out of range")
    
    contador = 0
    nodo_actual = lista.head
    while contador < index:
        nodo_actual = nodo_actual.to_right
        contador += 1
    
    return nodo_actual.value


def eliminar_nodo(index, lista):
        if index < 0:
            index = lista.size + index
        
        if index < 0 or index >= lista.size:
            raise IndexError("list index out of range")
        
        if index == 0:
            current_node = lista.head
            lista.head = current_node.to_right
            current_node.right = None
            return lista.imprimir()

        # if index == lista.size:
        #     contador = 0
        #     current_node = lista.head
        #     while contador < index - 1:
        #         current_node = current_node.to_right
        #         contador += 1

        #     delete_node =  current_node.to_right
        #     current_node.to_right = None
        #     delete_node.to_right = None
        #     return lista.imprimir()
        
        contador = 0
        current_node = lista.head
        while contador < index - 1:
            current_node = current_node.to_right
            contador += 1
        
        delete_node =  current_node.to_right
        current_node.to_right =  None if index == lista.size - 1 else delete_node.to_right 
        delete_node.to_right = None
        return lista.imprimir()
        

lista = my_li.ListaSencilla()
lista.insert_node('A')
lista.insert_node('B')
lista.insert_node('C')
lista.insert_node('D')
lista.insert_node('E')
lista.insert_node('F')
lista.insert_node('G')
print(lista.imprimir())

print(acceder_a_nodo(0, lista))

print(eliminar_nodo(0, lista))
print(eliminar_nodo(5, lista))
print(eliminar_nodo(2, lista))
