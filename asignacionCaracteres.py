print("asigancion:")
mensaje = "Hola"
mensaje += " "
mensaje += "Victor"

print(mensaje)

print("concatenacion:")
mensaje = "Hola"
espacio = " "
nombre = "Victor"

print(mensaje + espacio + nombre)

numeroUno = 4
numeroDos = 6
resultado =  numeroUno + numeroDos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado) 

print("busqueda:")
mensaje = "Hola Victor"
buscar_subcadena = mensaje.find("Victor")
print(buscar_subcadena)

print("extraccion:")
mensaje =  "Hola Victor"
extraer_subcadena = mensaje[5:11]
print(extraer_subcadena)

print("coomparacion")
mensajeUno = "Hola"
mensajeDos = "Hola"
mensajeTres = "Victor"
print(mensajeUno == mensajeDos)
print(mensajeDos == mensajeTres)
