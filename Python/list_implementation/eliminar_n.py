import implementacion_lista as my_li 

def eliminar_n_de_lista(n, lista):
    current_node = lista.head
    contador = 0
    while current_node:
        if current_node.value == n:
            current_node = current_node.to_right
            lista.remove_node_by_index(contador)
            continue
        current_node = current_node.to_right
        contador += 1
    
    return lista

lista_de_numeros = my_li.Lista()
lista_de_numeros.insert_node(4)
lista_de_numeros.insert_node(8)
lista_de_numeros.insert_node(5)
lista_de_numeros.insert_node(4)
lista_de_numeros.insert_node(16)
lista_de_numeros.insert_node(3)
lista_de_numeros.insert_node(42)
lista_de_numeros.insert_node(4)
lista_de_numeros.insert_node(60)
print(lista_de_numeros.imprimir())

lista_de_numeros = eliminar_n_de_lista(4, lista_de_numeros)

print(lista_de_numeros.imprimir())
