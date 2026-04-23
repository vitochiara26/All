class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Estoy hablando...")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, sueldo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.sueldo = sueldo

    def trabajar(self):
        print("Estoy trabajando...")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

    def estudiar():
        print("Estoy estudiando...")

humano = Empleado("Victor", 26, "Italiano", "Perrero", "30$")

humano.hablar()