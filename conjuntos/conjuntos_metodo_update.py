'''Agregar elementos a un conjunto con el metodo update'''
colores = {"verde","rojo", "azul"}
print("Conjunto colores: ", colores, "\n")

nuevos_colores = ["amarillo", "morado", "azul"]
print("Lista de nuevos colores: ", nuevos_colores, "\n")

colores.update(nuevos_colores)

print("Conjunto colores actualizado: ", colores, "\n")
