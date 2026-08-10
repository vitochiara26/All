import implementacion_lista as my_li

def imprimir_ms_desde_i(m, i, lista):
    if m == 0 or lista.head is None:
        return '[]'
    
    contador = 0
    nodo_actual = lista.head
    
    while True:
        if contador < i:
            contador += 1
            nodo_actual = nodo_actual.to_right
        else:
            lista_str = '['
            if m > 0:
                for _ in range(m-1):
                    lista_str += f'{nodo_actual.value}, '
                    nodo_actual = nodo_actual.to_right

                lista_str += f'{nodo_actual.value}'
                lista_str += ']' 
                break
            else:
                for _ in range(abs(m-1)):
                    lista_str += f'{nodo_actual.value}, '
                    nodo_actual = nodo_actual.to_left

                lista_str += f'{nodo_actual.value}]'
                break
    
    return lista_str

lista_abc = my_li.ListaCircular()
lista_abc.insert_node('A')
lista_abc.insert_node('B')
lista_abc.insert_node('C')
lista_abc.insert_node('D')
lista_abc.insert_node('E')
lista_abc.insert_node('F')
lista_abc.insert_node('G')
lista_abc.insert_node('H')
lista_abc.insert_node('I')
lista_abc.insert_node('J')
lista_abc.insert_node('K')
lista_abc.insert_node('L')
lista_abc.insert_node('M')
lista_abc.insert_node('N')
lista_abc.insert_node('O')
lista_abc.insert_node('P')
lista_abc.insert_node('Q')
lista_abc.insert_node('R')
lista_abc.insert_node('S')
lista_abc.insert_node('T')
lista_abc.insert_node('U')
lista_abc.insert_node('V')
lista_abc.insert_node('W')
lista_abc.insert_node('X')
lista_abc.insert_node('Y')
lista_abc.insert_node('Z')

print(lista_abc.imprimir())
print(imprimir_ms_desde_i(-10, 20, lista_abc))
