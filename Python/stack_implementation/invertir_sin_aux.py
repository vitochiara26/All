import imp_pila as pilita

def invertir_pila(pila, contador):
        if pila.size == contador:
            return pila
        top_de_pila_actual = pila.pop_node()
        nuevo_tope_de_pila = pila.pop_node()
        pila.push_node(top_de_pila_actual)
        invertir_pila(pila, contador)
        pila.push_node(nuevo_tope_de_pila) 


pila_pilita = pilita.Pila()
pila_pilita.push_node(1) 
pila_pilita.push_node(2)
pila_pilita.push_node(3)
print(pila_pilita.imprimir())

indice = 0
contador = 1
while indice < pila_pilita.size:
    invertir_pila(pila_pilita, contador)
    indice += 1
    contador += 1
    
print(pila_pilita.imprimir())