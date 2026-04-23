class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

def hacerSonido(animal):
    return animal.sonido()

perrito = Perro()
gatito = Gato()

print(perrito.sonido())
print(gatito.sonido())

print(hacerSonido(perrito))
print(hacerSonido(gatito))

