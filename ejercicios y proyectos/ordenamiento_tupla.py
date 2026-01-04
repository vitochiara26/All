'''Ordenamiento de una tupla'''
#Mi solucion
personas = (("Eduardo", 26), ("Maria", 30), ("Gerardo", 20), ("Valentina", 22))
print(f"Tupla original: {personas}\n")

list_personas = list(personas)
list_personas = sorted(list_personas, key = lambda persona: persona[1] )
personas_orden = tuple(list_personas)

print(f"La persona de menor edad es: {personas_orden[0]}")
print(f"la persona de mayor edad es: {personas_orden[-1]}")



#Solucion del profesor
personas = (("Eduardo", 26), ("Maria", 30), ("Gerardo", 20), ("Valentina", 22))
print(personas)

personas = list(personas)
longitud_lista = len(personas)

for i in range(longitud_lista-1):
    #print(personas[i][1])
    for j in range(i + 1,longitud_lista):
        #print(personas[j][1])
        if personas[i][1] > personas[j][1]:
            aux = personas[i]
            personas[i] = personas[j]
            personas[j] = aux
            #print("Sucede orden\n")
        #else:
            #print("No sucede orden\n")
print(f"La persona de menor edad es: {personas[0]}")
print(f"La persona de mayor edad es: {personas[-1]}")
