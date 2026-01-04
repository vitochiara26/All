frase = input("Introduce una frase: ")
eliminar = input("Introduce la palabra que deseas eliminar?: ")

indice= frase.find(eliminar)
substring = frase[ :indice] + frase[indice + (len(eliminar) + 1): ]
print(substring)
