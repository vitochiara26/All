import implementacion_lista as my_li 

def mezclar_listas(lista_uno, lista_dos):
    lista_tres = my_li.Lista()
    inspected_node_l1 = lista_uno.head
    inspected_node_l2 = lista_dos.head
    i = 0
    j = 0
    
    while i < lista_uno.size and j < lista_dos.size:
        if inspected_node_l1.value < inspected_node_l2.value:
            lista_tres.insert_node(inspected_node_l1.value)
            i += 1
            inspected_node_l1 = inspected_node_l1.to_right
        else:
            lista_tres.insert_node(inspected_node_l2.value)
            j += 1
            inspected_node_l2 = inspected_node_l2.to_right
    
    if i < lista_uno.size:
        while inspected_node_l1:
            lista_tres.insert_node(inspected_node_l1.value)
            inspected_node_l1 = inspected_node_l1.to_right
    if j < lista_dos.size:
        while inspected_node_l2:
            lista_tres.insert_node(inspected_node_l2.value)
            inspected_node_l2 = inspected_node_l2.to_right
    
    return lista_tres
    

lista_uno = my_li.Lista()
lista_uno.insert_node(0)
lista_uno.insert_node(2)
lista_uno.insert_node(4)
lista_uno.insert_node(6)
lista_uno.insert_node(8)
print(lista_uno.imprimir())

lista_dos = my_li.Lista()
lista_dos.insert_node(1)
lista_dos.insert_node(3)
lista_dos.insert_node(5)
lista_dos.insert_node(7)
lista_dos.insert_node(9)
print(lista_dos.imprimir())

lista_tres = mezclar_listas(lista_uno, lista_dos)
print(lista_tres.imprimir())
