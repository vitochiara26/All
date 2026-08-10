import imp_pila as pilita

def sumar_topes(pila_uno, pila_dos, pila_aux, acumulado = 0):
    if not pila_uno.top or not pila_dos.top:
            return
    tope_pila_uno = pila_uno.pop_node() 
    tope_pila_dos = pila_dos.pop_node()
    
    nuevo_tope = (tope_pila_uno + tope_pila_dos) + acumulado
    acumulado = nuevo_tope // 10
    resto = nuevo_tope % 10
    pila_aux.push_node(resto)
    
    sumar_topes(pila_uno, pila_dos, pila_aux, acumulado)

def invertir_pila(pila_uno, pila_dos):
    if not pila_uno.top:
        return
    
    tope_pila_uno = pila_uno.pop_node()
    pila_dos.push_node(tope_pila_uno)
    
    invertir_pila(pila_uno, pila_dos)


pila_uno = pilita.Pila()
pila_uno.push_node(1)
pila_uno.push_node(4)
pila_uno.push_node(5)
print(pila_uno.imprimir())

pila_dos = pilita.Pila()
pila_dos.push_node(5)
pila_dos.push_node(3)
pila_dos.push_node(5)
print(pila_dos.imprimir())

pila_aux = pilita.Pila()
sumar_topes(pila_uno, pila_dos, pila_aux)

pila_tres = pilita.Pila()
invertir_pila(pila_aux, pila_tres)
print(pila_tres.imprimir())
