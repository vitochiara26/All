class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_name):
        self.__nombre = new_name

victor = Persona("Victor" , 26)

nombre = victor.get_nombre()
print(nombre)

victor.set_nombre("Victoria")

nombre = victor.get_nombre()
print(nombre)
