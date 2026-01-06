def funcion_combinada(*args, **kwargs):
    print("Argumentos posicionales: ", args)
    print("Argumentos de palabra clave: ", kwargs)


funcion_combinada(1, 2, 3, nombre="Victor", edad=26)