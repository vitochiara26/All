def saludar(nombre, saludo):
    mensaje = f"¡{saludo}, {nombre}!"
    print(mensaje)


saludar("Ana", "Hola")
saludar(saludo="Hola", nombre="Ana")
