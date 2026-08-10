import imp_pila as pilita

def es_palin(pila_evaluada):
    pila_aux = pilita.Pila()
    pila_invertida = pilita.Pila()
    
    while pila_evaluada.top:
        valor_de_plato = pila_evaluada.pop_node()
        pila_invertida.push_node(valor_de_plato)
        pila_aux.push_node(valor_de_plato)
    
    while pila_aux.top:
        pila_evaluada.push_node(pila_aux.pop_node())
    
    es_palin = True
    
    while pila_evaluada.top:
        valor_al_derecho = pila_evaluada.pop_node()
        valor_al_revez = pila_invertida.pop_node()
        
        if valor_al_derecho != valor_al_revez:
            es_palin = False
        
        pila_aux.push_node(valor_al_derecho)
    
    while pila_aux.top:
        pila_evaluada.push_node(pila_aux.pop_node())
    
    return es_palin

pila_original = pilita.Pila()
pila_original.push_node('Y')
pila_original.push_node('O')
pila_original.push_node('S')
pila_original.push_node('O')
pila_original.push_node('Y')

print(pila_original.imprimir())

print(es_palin(pila_original))

print(pila_original.imprimir())
