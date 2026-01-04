'''importar modulos'''
#Importar un modulo completo
import math
print(math.sqrt(25))
print(math.sin(30))

#Importar un modulo con un alias

import math as m
print(m.sqrt(25))
print(m.tan(30))

#Importar solo lo necesario de un modulo
from math import sqrt, sin
print(sqrt(25))
print(sin(30))

#Importar todo de un modelo (Evitar esta practica)

from math import *
print(sqrt(25))
print(sin(30))
print(tan(30))
