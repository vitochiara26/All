class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara =  camara


celular_1 = Celular("Samsung", "S23", "48MP")

print(celular_1.marca)
print(celular_1.modelo)
print(celular_1.camara)
