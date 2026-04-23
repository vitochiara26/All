def decorador(funcion):
    def funcionModificada():
        print("Antes de llamar a la funcion")
        funcion()
        #print("Despues de llamar a la funcion")
    return funcionModificada

# def saludo():
#     print("Hola Victor")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola Victor")

saludo()