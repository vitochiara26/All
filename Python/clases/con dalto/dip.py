# class Diccionario:
#     def verificarPalabra(self, palabra):
#         #logica para verificar palabras
#         pass


# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregirTexto():
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #logica para verificar si una palabra está en el diccionario
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar si una palabra está en el diccionario
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar si una palabra está en el diccionario
        pass

class CorectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #usamos el verificador para corregir texto
        pass


corrector = CorectorOrtografico(Diccionario)
