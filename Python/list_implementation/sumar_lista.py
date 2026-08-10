import implementacion_lista as my_li

def sumar_lista(lista):
    sum = 0
    current_node = lista.head
    while current_node:
        sum += current_node.value
        current_node = current_node.to_right
    return sum

lista_a_sumar = my_li.Lista()
lista_a_sumar.insert_node(10)
lista_a_sumar.insert_node(20)
lista_a_sumar.insert_node(30)
lista_a_sumar.insert_node(40)
lista_a_sumar.insert_node(50)
lista_a_sumar.insert_node(60)

print(lista_a_sumar.imprimir())

resultado_suma = sumar_lista(lista_a_sumar)
print(resultado_suma)
