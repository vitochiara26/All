import imp_pila as pil


def eliminar_x_nodos(pila_ori, p, d):
    if p < 0 or d <0:
        raise ValueError("La posición P y el desplazamiento d deben ser mayores o iguales a 0")
    
    pila_aux = pil.Pila()
    
    while pila_ori.top:
        pila_aux.push_node(pila_ori.pop_node())
    
    indice = 0
    
    while pila_aux.top:
        elemento = pila_aux.pop_node()
        
        if indice == p or indice == (p + d):
            pass
        else: 
            pila_ori.push_node(elemento)
        
        indice += 1
    
    return pila_ori


pila_original = pil.Pila()
pila_original.push_node(00)
pila_original.push_node(10)
pila_original.push_node(20)
pila_original.push_node(30)
pila_original.push_node(40)
pila_original.push_node(50)
print(pila_original.imprimir())

eliminar_x_nodos(pila_original, 1, 2)

print(pila_original.imprimir())
