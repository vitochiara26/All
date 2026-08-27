import imp_pila as pil


def sumar_par_de_elementos(pila):
    if pila.size < 2:
        return
    
    res_par_elem = pila.pop_node()
    res_par_elem += pila.pop_node()
    
    sumar_par_de_elementos(pila)
    pila.push_node(res_par_elem)


elementos = pil.Pila()
elementos.push_node(5)
elementos.push_node(4)
elementos.push_node(3)
elementos.push_node(2)
elementos.push_node(1)
print(elementos.imprimir())

sumar_par_de_elementos(elementos)
print(elementos.imprimir()) 