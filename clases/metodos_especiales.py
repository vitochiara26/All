'''Metodos especiales dentro de las clases'''
class Book:
    '''Crear un libro'''
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))
print(len(book2))
print(str(book1))
print(str(book2))
print(book1 == book2)

class Cart:
    '''Crear un carrito de compras'''
    def __init__(self):
        self.items = []

    def add(self, item):
        '''agrega articulos al carrito'''
        self.items.append(item)

    def remove(self, item):
        '''quita un articulo si se encuentra en el carrito'''
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in cart")

    def list_items(self):
        '''Regresa la lista de la articulos en el carrito'''
        return self.items

    def __len__(self):
        '''Regresa cuantos articulos hay en el carrito'''
        return len(self.items)

    def __getitem__(self, index):
        '''Regresa el lugar especifico del articulo en el carrito'''
        return self.items[index]

    def __contains__(self, item):
        '''Regresa si el articulo buscado esta en el carrito'''
        return item in self.items

    def __iter__(self):
        '''Reccorre y muestra los articulos en el carrito'''
        return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
    print(item, end=' ')

print(f"\n{len(cart)}")
print(cart[3])

print('Monitor' in cart)
print('banana' in cart)

cart.remove('Ergo keyboard')

print(cart.list_items())

cart.remove('banana')
