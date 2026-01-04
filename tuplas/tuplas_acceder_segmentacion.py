'''Accediendo a los elementos de una tupla con el operador de segmentacion'''
tupla_vocales = ("a", "e", "i", "o", "u")
print(tupla_vocales, '\n')

print(f"Posiciones [0:2]: -> {tupla_vocales[0:2]}")
print(f"Posiciones [::2]: -> {tupla_vocales[::2]}")
print(f"Posiciones [-3:]: -> {tupla_vocales[-3:]}")
print(f"Posiciones [::-1]: -> {tupla_vocales[::-1]}")
