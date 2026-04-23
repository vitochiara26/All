from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacerActividad(self):
        pass

    def presentarse(self):
        print(f'Hola soy {self.nombre} y tengo {self.edad} años.')

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacerActividad(self):
        print(f'Estoy estudiando: {self.actividad}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacerActividad(self):
        print(f'Estoy trabajando: {self.actividad}')

victor = Estudiante("Victor", 26, "Masculino", "Programacion")
victor.presentarse()
victor.hacerActividad()

jose = Trabajador("José", 38, "Masculino", "Carpinteria")
jose.presentarse()
jose.hacerActividad()
