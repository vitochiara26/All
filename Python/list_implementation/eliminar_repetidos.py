import implementacion_lista as my_li

def verificar_repeticion(value, lista):
    current_node = lista.head
    while current_node:
        if current_node.value == value:
            return True
        else :
            current_node = current_node.to_right
    return False

def eliminar_repetidos(lista):
    new_lista = my_li.ListaSencilla()
    current_node = lista.head
    while current_node:
        if not verificar_repeticion(current_node.value, new_lista):
            new_lista.insert_node(current_node.value)
            current_node = current_node.to_right
        else:
            current_node = current_node.to_right
    
    return new_lista


lista_de_repetidos = my_li.ListaSencilla()
lista_de_repetidos.insert_node(1)
lista_de_repetidos.insert_node(1)
lista_de_repetidos.insert_node(2)
lista_de_repetidos.insert_node(2)
lista_de_repetidos.insert_node(2)
lista_de_repetidos.insert_node(3)
lista_de_repetidos.insert_node(4)
lista_de_repetidos.insert_node(4)
lista_de_repetidos.insert_node(5)
lista_de_repetidos.insert_node(5)
lista_de_repetidos.insert_node(5)
print(lista_de_repetidos.imprimir())

lista_sin_repetidos = eliminar_repetidos(lista_de_repetidos)
print(lista_sin_repetidos.imprimir())
