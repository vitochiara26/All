class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando...")

nombre = input("Indique su nombre: ").capitalize()
edad = input("Ahora indique su edad: ")
grado = input("por ultimo indique su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f""" 
    Datos del estudiante: \n
    Nombre: {estudiante.nombre}
    Edad: {estudiante.edad} 
    Grado: {estudiante.grado}
""")

while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break
