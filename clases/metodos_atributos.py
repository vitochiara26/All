'''Metodos y atributos de las clases y objetos'''
class Dog:
    '''Crear perro'''
    species = "French Bulldog" #Atributo de clase

    def __init__(self, name):
        self.name = name #Atributo de instancia

    def bark(self):
        '''Ladra'''
        return f"{self.name} says woof woof"

print(Dog.species)

dog1 = Dog("Jack")
print(dog1.name)
print(dog1.species)

dog2 = Dog("Tom")
print(dog2.name)
print(dog2.species)

print(dog1.bark())
print(dog2.bark())

class Car:
    '''Crear un carro'''
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def describe(self):
        '''Describe'''
        return f"This car is a {self.color} {self.model}"
car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model)
print(car_2.model)

print(car_1.color)
print(car_2.color)

print(car_1.describe())
print(car_2.describe())
