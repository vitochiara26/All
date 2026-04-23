class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Estoy hablando...")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        return f'Mi habilidad es: {self.habilidad}'

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, sueldo, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.sueldo = sueldo
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola soy {self.nombre}, tengo {self.edad} años, soy {self.nacionalidad},',end="")
        print(f' {(super().mostrarHabilidad()).lower()}, ', end="")
        print(f'trabajo en {self.empresa} y gano {self.sueldo} a la semana.')

humano = EmpleadoArtista("victor", 26, "italiano", "programar","30$", "Lynos")
cantante = Artista("Cantar")

humano.presentarse()
print(cantante.mostrarHabilidad())

#herencia = issubclass(Artista, Persona)
objeto = isinstance(humano, EmpleadoArtista)
print(isinstance(cantante, Artista))
print(objeto)