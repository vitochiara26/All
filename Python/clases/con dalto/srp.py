class Auto():
    def __init__(self, tanque):
        self.position = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtenerCombustible() >= distancia/2:
            self.position += distancia
            self.tanque.usarCombustible(distancia / 2)
            return "El auto se ha movido"
        else:
            return "No hay suficiente combustible"

    def obtenerPosicion(self):
        return self.position

class TanqueCombustible:
    def __init__(self):
        self.combustible = 100

    def agregarCombustible(self, cantidad):
        self.combustible += cantidad

    def obtenerCombustible(self):
        return self.combustible
    
    def usarCombustible(self, cantidad):
        self.combustible -= cantidad


tanque = TanqueCombustible()
carro = Auto(tanque)

print(carro.obtenerPosicion())
print(carro.mover(10))

print(carro.obtenerPosicion())
print(carro.mover(20))

print(carro.obtenerPosicion())
print(carro.mover(60))

print(carro.obtenerPosicion())
print(carro.mover(100))

print(carro.obtenerPosicion())
print(carro.mover(100))
