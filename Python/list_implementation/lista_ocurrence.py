import implementacion_lista as my_li 

def verificar_repeticion(value, lista):
    current_node = lista.head
    while current_node:
        if current_node.value == value:
            return True
        else :
            current_node = current_node.to_right
    return False

def contar_repetidos(value, lista):
    current_node = lista.head
    occurrence = 0
    while current_node:
        if current_node.value == value:
            occurrence += 1
            current_node = current_node.to_right
        else:
            current_node = current_node.to_right
    return occurrence

def insertar_repetidos(lista):
    lista_sin_repetidos = my_li.Lista()
    current_node = lista.head
    while current_node:
        if not verificar_repeticion(current_node.value, lista_sin_repetidos):
            lista_sin_repetidos.insert_node(current_node.value)
            repeticiones_de_valor =  contar_repetidos(current_node.value, lista_repetidos)
            lista_sin_repetidos.insert_node(str(f"'{repeticiones_de_valor}'"))
            current_node = current_node.to_right
        else:
            current_node = current_node.to_right
    
    return lista_sin_repetidos

lista_repetidos = my_li.Lista()
lista_repetidos.insert_node(3)
lista_repetidos.insert_node(4)
lista_repetidos.insert_node(2)
lista_repetidos.insert_node(4)
lista_repetidos.insert_node(4)
lista_repetidos.insert_node(1)
lista_repetidos.insert_node(2)
lista_repetidos.insert_node(1)
lista_repetidos.insert_node(5)
lista_repetidos.insert_node(3)
lista_repetidos.insert_node(1)

lista_sin_rep_con_occu = insertar_repetidos(lista_repetidos)
print(lista_sin_rep_con_occu.imprimir())
