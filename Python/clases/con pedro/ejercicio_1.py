class Biblioteca:
    def __init__(self, posiciones, ancho, alto):
        self.__posiciones = ['']*posiciones
        self.__ancho = ancho
        self.__alto = alto
    
    def get_posiciones(self):
        return self.__posiciones
    
    def set_posiciones(self,valor):
        self.__posiciones = ['']*valor
    
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self, valor):
        self.__ancho = valor
    
    def get_alto(self):
        return self.__alto
    
    def set_alto(self, valor):
        self.__alto = valor

    def mostar_libros(self):
        print(f"La biblioteca tiene los siguientes libros: ")
        print("| ", end="")
        for l in self.get_posiciones():
            if l == '':
                print("           ", end=" | ")
            else :
                print(l, end=" | ")
        print()
    
    def mostrar_biblioteca(self):
        print(f"La biblioteca tiene {self.get_alto()}" 
            " metros de alto y {self.get_ancho()} metros de ancho")
    

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, valor):
        self.__nombre = valor
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, valor):
        self.__nombre = valor
    
    def get_sexo(self):
        return self.__sexo
    
    def set_sexo(self, valor):
        self.__sexo = valor
        
    def sacar_libro(self, posicion, biblioteca):
        libro = biblioteca.get_posiciones()[posicion-1]
        biblioteca.get_posiciones()[posicion-1] = ''
        print(f"Sacaste el libro '{libro}' de la poscion {posicion} del estante")
    
    def meter_libro(self, libro, posicion, biblioteca):
        biblioteca.get_posiciones()[posicion-1] = libro.get_portada()
        print(f"Metiste el libro '{libro.get_portada()}' en la poscion {posicion} del estante")

class Libro:
    def __init__(self, cantidad_hojas, empastado, portada):
        self._cantidad_hojas = cantidad_hojas
        self._empastado = empastado
        self._portada = portada
    
    def get_cantidad_hojas(self):
        return self._cantidad_hojas
    
    def set_cantidad_hojas(self, valor):
        self._cantidad_hojas = valor
    
    def get_empastado(self):
        return self._empastado
    
    def set_empastado(self, valor):
        self._empastado = valor
    
    def get_portada(self):
        return self._portada
    
    def set_portada(self, valor):
        self._portada = valor
    
    def sentir_empastado(self):
        print(f'El libro tiene un empastado de tipo de tipo: {self.get_empastado()}')

    def revisar_contenido(self):
        print(f'El libro tiene mucho contenido en sus {self.get_cantidad_hojas()} hojas.')


class Enciclopedia(Libro):
    def __init__(self, cantidad_hojas, empastado, portada, indice, contenido, encuadernado):
        super().__init__(cantidad_hojas, empastado, portada)
        self._indice = indice
        self._contenido = contenido
        self._encuadernado = encuadernado
    
    def get_indice(self):
        return self._indice
    
    def set_indice(self, valor):
        self._indice = valor
    
    def get_contenido(self):
        return self._contenido
    
    def set_contenido(self, valor):
        self._contenido = valor
    
    def get_encuaderno(self):
        return self._encuadernado
    
    def set_encuaderno(self, valor):
        self._encuadernado = valor
    
    def sentir_empastado(self):
        print(f'La Enciclopedia tiene un empastado de tipo de tipo: {self.get_empastado()}')

    def revisar_contenido(self):
        print(f'La Enciclopedia tiene mucho contenido en sus {self.get_cantidad_hojas()} hojas.')
    
    def mostar_contenido(self):
        print(f'El contenido de la enciclopedia habla sobre: {self.get_contenido()}')
    
    def ver_indice(self):
        print(f'El indice de la Enciclopedia muestra sus {self.get_indice} secciones')


class Cuaderno(Libro):
    def __init__(self, cantidad_hojas, empastado, portada, materia, contenido, encuadernado):
        super().__init__(cantidad_hojas, empastado, portada)
        self._materia = materia
        self._contenido = contenido
        self._encuadernado = encuadernado
    
    def get_materia(self):
        return self._materia
    
    def set_materia(self, valor):
        self._materia = valor
    
    def get_contenido(self):
        return self._contenido
    
    def set_contenido(self, valor):
        self._contenido = valor
    
    def get_encuaderno(self):
        return self._encuadernado
    
    def set_encuaderno(self, valor):
        self._encuadernado = valor
    
    def sentir_empastado(self):
        print(f'El Cuaderno tiene un empastado de tipo de tipo: {self.get_empastado()}')

    def revisar_contenido(self):
        print(f'El Cuaderno tiene mucho contenido en sus {self.get_cantidad_hojas()} hojas.')
    
    def mostar_contenido(self):
        print(f'El contenido del Cuaderno: {self.get_contenido()}')
    
    def ver_materia(self): 
        print(f'El Cuaderno se usa para estudiar {self.get_materia()}')

victor = Persona("Victor", 26, "Femenino") #creo a la persona gay

biblioteca = Biblioteca(2, 3, 2) #creo la biblioteca 

libro = Libro(234, "Grueso", "Anatomia humana.") #creo un libro
print(f"El titulo es {libro.get_portada()}") #leo el titulo del libro

#creo una enciclopedia
enciclopedia = Enciclopedia(
    574,
    "Reforzado",
    "Biologia",
    9,
    "la ciencia que estudia la vida y los seres vivos.",
    "pegado con silicon"
)
enciclopedia.sentir_empastado()

#creo un cuaderno 
cuaderno = Cuaderno(
    100,
    "delgado", 
    "Apuntes de mate",
    "Matematicas",
    "apuntes sobre clases da matematicas",
    "Engrapado"
)
cuaderno.ver_materia() #reviso sobre que materia es el cuaderno

#decido guardar los 3 libros en la biblioteca pero tiene solo 2 espacios, le seteo un nuevo espacio
biblioteca.set_posiciones(3)

#el usuario guarda sus libros en la biblioteca
victor.meter_libro(libro, 1, biblioteca)
victor.meter_libro(enciclopedia, 2, biblioteca)
victor.meter_libro(cuaderno, 3, biblioteca)

#vemos los libros en la biblioteca
biblioteca.mostar_libros()

#el usuario ahora saca el cuaderno de matematicas para poder estudiar
victor.sacar_libro(3, biblioteca)
Cuaderno.mostar_contenido(cuaderno)

#vemos los libros quedaron en la biblioteca
biblioteca.mostar_libros()

#el usuario deja de estudiar matematicas
victor.meter_libro(cuaderno, 3, biblioteca)
#ahora va a leer una enciclopedia
victor.sacar_libro(1, biblioteca)

#vemos los libros quedaron en la biblioteca
biblioteca.mostar_libros()