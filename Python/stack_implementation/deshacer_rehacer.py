import imp_pila as pil


def vaciar_pila(pila):
    while pila.size > 0:
        pila.pop_node()

def realizar_accion(accion, pila_deshacer, pila_rehacer):
    pila_deshacer.push_node(accion)
    vaciar_pila(pila_rehacer)
    print(f"Accion ejecutada: {accion}")

def deshacer(pila_deshacer, pila_rehacer):
    if pila_deshacer.size == 0:
        print("No hay acciones que deshacer")
        return
    
    accion = pila_deshacer.pop_node()
    pila_rehacer.push_node(accion)
    print(f"<- Desecho: {accion}")
    return accion

def rehacer(pila_deshacer, pila_rehacer):
    if pila_rehacer.size == 0:
        print("No hay acciones que rehacer")
        return
        
    accion = pila_rehacer.pop_node()
    pila_deshacer.push_node(accion)
    print(f"<- Rehecho: {accion}")
    return accion


pila_deshacer = pil.Pila()
pila_rehacer = pil.Pila()

realizar_accion("Escribir: 'Hola'", pila_deshacer, pila_rehacer)
realizar_accion("Escribir: 'Mundo'", pila_deshacer, pila_rehacer)
realizar_accion("Aplicar Negrita", pila_deshacer, pila_rehacer)

deshacer(pila_deshacer, pila_rehacer)
deshacer(pila_deshacer, pila_rehacer)

rehacer(pila_deshacer, pila_rehacer)

realizar_accion("Escribir: 'Amigo'", pila_deshacer, pila_rehacer)

rehacer(pila_deshacer, pila_rehacer)
