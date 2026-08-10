import implementacion_lista as my_li

def dividir_pares_de_none(lista):
    new_lista = my_li.Lista()
    cuantos_pares = 0
    current_node = lista.head
    
    while current_node:
        if current_node.value % 2 == 0:
            new_lista.insert_node(current_node.value, cuantos_pares)
            cuantos_pares += 1
            current_node = current_node.to_right
        else:
            new_lista.insert_node(current_node.value)
            current_node = current_node.to_right
    
    return new_lista

lista_pare_none = my_li.Lista()
lista_pare_none.insert_node(0)
lista_pare_none.insert_node(1)
lista_pare_none.insert_node(2)
lista_pare_none.insert_node(3)
lista_pare_none.insert_node(4)
lista_pare_none.insert_node(5)
lista_pare_none.insert_node(6)
lista_pare_none.insert_node(7)
lista_pare_none.insert_node(8)
lista_pare_none.insert_node(9)

print(lista_pare_none.imprimir())
lista_dividida = dividir_pares_de_none(lista_pare_none)
print(lista_dividida.imprimir())