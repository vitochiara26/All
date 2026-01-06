y = 20


def funcion():
    global y
    y = 30
    print(y, "Impresión dentro de la función")


funcion()
print(y, "Impresión fuera de la función")
