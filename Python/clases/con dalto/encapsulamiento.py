class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"
        self.__atributo_muy_privado = "Contraseña"


objeto = MiClase()

print(objeto._atributo_privado)
print(objeto.__atributo_muy_privado)
