class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("El animal esta volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Murcielago(Ave, Mamifero):
    pass

vampiro = Murcielago()
vampiro.comer()
vampiro.volar()
vampiro.amamantar()

print(Murcielago.mro())
