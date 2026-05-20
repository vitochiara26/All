def is_balanced(message):
    tamaño_mensaje = len(message)
    mitad_mensaje = tamaño_mensaje // 2
    
    primera_mitad_mensaje = message[:mitad_mensaje]
    if tamaño_mensaje % 2 == 0:
        segunda_mitad_mensaje = message[mitad_mensaje:]
    else:
        segunda_mitad_mensaje = message[mitad_mensaje+1:]
        
    vocales_primera_mitad = 0
    for letra in primera_mitad_mensaje:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            vocales_primera_mitad += 1
    
    vocales_segunda_mitad = 0
    for letra in segunda_mitad_mensaje:
        if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
            vocales_segunda_mitad += 1
    
    if vocales_primera_mitad == vocales_segunda_mitad:
        return True
    
    return False

print(is_balanced("racecar"))
print(is_balanced("Lorem Ipsum"))
print(is_balanced("Kitty Ipsum"))
