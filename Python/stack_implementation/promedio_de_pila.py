import imp_pila as pil

def promedio(pila):
    sumas = 0
    resultado = 0

    while pila.top:
        resultado += pila.pop_node()
        sumas += 1
    
    return resultado / sumas


pila_normal = pil.Pila()
pila_normal.push_node(1)
pila_normal.push_node(2)
pila_normal.push_node(3)
pila_normal.push_node(4)
pila_normal.push_node(5)

print(promedio(pila_normal))
