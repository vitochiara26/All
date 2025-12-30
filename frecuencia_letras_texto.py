'''programa que ingresa la frecuencia de letras utilizadas en un texto'''
frase = input("Ingresa un texto: ")

dictionary = {}

for letra in frase:
    dictionary.update({letra:frase.count(letra)})

print(dictionary)

string = input("Ingresa un texto: ")

letters = dict.fromkeys(string, 0)

for letter in string:
    letters[letter] += 1

print(letters)

