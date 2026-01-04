'''Eliminar elementos de un conjunto con los metodos remove() y discard()'''
#Metodo remove()
vocales = {'a', 'e', 'i', 'o','u'}
print(vocales)
vocales.remove('i')
print(vocales, '\n')


#metodo discard():
vocales = {'a', 'e', 'i', 'o','u'}
print(vocales)
vocales.discard('i')
vocales.discard('x')
print(vocales, '\n')

#Evitar errror con el metodo remove():
vocales = {'a', 'e', 'i', 'o','u'}
print(vocales)

element = "u"
if element in vocales:
    vocales.remove(element)
    print(vocales)
else:
    print(f"'{element}' no esta en el conjunto vocales.")
