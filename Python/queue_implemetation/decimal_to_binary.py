import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import stack_implementation.imp_pila as pil
import queue_imp as que

def decimal_a_binario_cola(pila_decimal):
    if pila_decimal.size == 0:
        raise IndexError("La pila está vacia.")
    
    #1. extraer el numero de la pila de entrada
    numero = int(pila_decimal.pop_node())
    
    cola_binaria = que.Cola()
    
    #si el numero es 0
    if numero == 0:
        cola_binaria.enqueue_node(0)
        return cola_binaria
    
    pila_residuos = pil.Pila()
    
    #2. Divisiones sucesivas entre 2 guardando los residuos
    temp = abs(numero)
    while temp > 0:
        residuo = temp % 2
        pila_residuos.push_node(residuo)
        temp //= 2
    
    #3. desapilar los bits
    while pila_residuos.size > 0:
        cola_binaria.enqueue_node(pila_residuos.pop_node())
    
    return cola_binaria


pila_entrada = pil.Pila()
pila_entrada.push_node(36)

print("Pila de entrada (número decimal):")
print(pila_entrada.imprimir())

cola_resultado = decimal_a_binario_cola(pila_entrada)

print("\nCola resultado (representación binaria):")
print(cola_resultado.imprimir())