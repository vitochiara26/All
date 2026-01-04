'''Funcion enumerate() para recorrer elementos de
un iterable miebtras se lleva un contador de la posicion de cada elemento'''

frutas = ['manzana', 'platano', 'uva', 'sandia']
print(frutas, '\n')

#Recorrido con for
for posicion, fruta in enumerate(frutas):
    print(f"Posicion {posicion}: {fruta}")

print('\n')

enumerado = list(enumerate(frutas, start=1))
print(enumerado)
