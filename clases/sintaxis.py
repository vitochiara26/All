'''Sintaxis para la creacion de una clase'''
class ClassName:
    '''Clase representando un nombre'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_metod(self):
        '''Imprimir el name en mayuscula'''
        print(self.name.upper())

class Dog:
    '''Creando un perro'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        '''Ladrar'''
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

#object_1 = ClassName(attribute_1, attribute_2)
#object_2 = ClassName(attribute_1, attribute_2)

#object_1.method_name()
#object_2.method_name()

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

dog_1.bark()
dog_2.bark()
