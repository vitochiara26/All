import implementacion_lista as my_li 

def sumar_lista(lista):
    if lista.size % 2 == 0 :
        if lista.size == 2:
            return lista.search_node_value(0) + lista.search_node_value(1)

        return (lista.search_node_value(0) +
                lista.search_node_value(1) +
                sumar_lista(lista.segment_list(2,lista.size)))
    else:
        if lista.size == 1:
            return lista.search_node_value(0)

        return (lista.search_node_value(0) +
                lista.search_node_value(1) +
                sumar_lista(lista.segment_list(2,lista.size)))
        

lista_a_sumar = my_li.Lista()
lista_a_sumar.insert_node(10)
lista_a_sumar.insert_node(20)
lista_a_sumar.insert_node(30)
lista_a_sumar.insert_node(40)
lista_a_sumar.insert_node(50)
lista_a_sumar.insert_node(60)
lista_a_sumar.insert_node(70)

print(lista_a_sumar.imprimir())

resultado_suma = sumar_lista(lista_a_sumar)
print(resultado_suma)
