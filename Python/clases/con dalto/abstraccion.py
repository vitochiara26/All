class Auto:
    def __init__(self):
        self.__estado = "Apagado"
    
    def encender(self):
        self.__estado = "Encendido"
        print("Start engine")

    def conducir(self):
        if self.__estado == "Apagado":
            self.encender()
        print("Conduciendo el auto")

mi_auto = Auto()
mi_auto.conducir()