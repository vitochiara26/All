class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrarGrado(self):
        print(f'Grado: {self.grado}')

estudiante = Estudiante("Victor", 26, "6to semestre")
estudiante.mostrarDatos()
estudiante.mostrarGrado()