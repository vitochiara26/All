import implementacion_lista as my_li 

def invertir_iterativa(lista):
    for indice in range(lista.size - 1, -1, -1):
        print(lista.search_node(indice), end=', ')
    print('\n')

def invertir_recursiva(lista, contador = 0):
    if contador < lista.size -1:
        invertir_recursiva(lista, contador + 1)
    
    print(lista.search_node(contador), end=', ')

lista_usada = my_li.ListaSencilla()
lista_usada.insert_node('A');
lista_usada.insert_node('B');
lista_usada.insert_node('C');
lista_usada.insert_node('D');
lista_usada.insert_node('E');

print(lista_usada.imprimir())
# invertir_iterativa(lista_usada)

invertir_recursiva(lista_usada)
