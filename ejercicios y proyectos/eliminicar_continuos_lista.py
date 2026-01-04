lista = ["A", "B", "b", "c", "E", "E", "f"]
print(f"Lista original: {lista}")
elemento_eliminar = input("Introduce el elemnto que deseas eliminar: ")
nueva_lista = []

for elemento_lista in lista :
    if elemento_eliminar.lower() != elemento_lista.lower() :
        nueva_lista.append(elemento_lista)
        
print(f"Elemento eliminado: {nueva_lista}")