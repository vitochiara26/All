'''Manejar atributos de objetos dinamicamente'''
class Car:
    '''Crea un carro'''
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car('Lamborghini', 'Gallardo')
print(my_car.brand)
print(my_car.model)
print("")

#getattr()
#getattr(object, attribute_name, default_value)
class Person:
    '''crea una persona'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Jhon Doe', 30)

#print(getattr(person, 'name'))
#print(getattr(person, 'age'))
#print(getattr(person, 'city', 'Milano'))

#attr_name = input('Enter the attribute you want to see: ')
#print(getattr(person, attr_name, 'Atribute not found'))

for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')
print("")

#setattr()
#setattr(object, attribute_name, value)

class Configuration:
    '''Crea una configuracion vacia'''
    pass


settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

#print(config_obj.server_url)
#print(config_obj.timeout_sec)

#hasattr()
#hasattr(object, attribute_name)

class Product:
    '''Crea un producto'''
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')
print("")

#delattr
#delattr(object, attribute_name)

class UserSession:
    '''Crea el inicio de sesion de un usuario'''
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token #valor sensible
        self.temp_counter = 0 #valor tempral

session = UserSession(101, 'a1b2c3d3e5')

#Lista de atributos a borrar
attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')
