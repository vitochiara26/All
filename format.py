#Alternativa 1
nombre = "Carlos"
edad = 22
print("Hola {}, tienes {} años.".format(nombre, edad))

#Alternativa 2
nombre = "Carlos"
edad = 22
print("Hola {nombre}, tienes {edad} años.".format(nombre = "Carlos", edad = 22))

#Alternativa 3
nombre = "Carlos"
edad = 22
print("Hola {0}, tienes {1} años.".format(nombre, edad))
print("Hola {1}, tienes {0} años.".format(edad, nombre))
