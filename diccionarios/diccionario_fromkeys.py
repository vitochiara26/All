'''El metodo fromkeys para crear diccionarios con valores predeterminados'''
#Secuencia con lista sin valor asignado
sequence = ["uno", "dos", "tres"]
name_dic = dict.fromkeys(sequence)
print("Secuencia con lista sin valor: ", name_dic)

#Secuencia con lista con valor asignado
sequence = ["uno", "dos", "tres"]
value = 5
name_dic = dict.fromkeys(sequence, value)
print("\nSecuencia con lista y valor: ", name_dic)

#Secuencia con diccionario
sequence = {"uno": 1,
            "dos": 2,
            "tres": 3
            }
value = 5
name_dic = dict.fromkeys(sequence, value)
print("\nSecuencia con diccionario y valor: ", name_dic)

#secuencia con texto
name_dic = {}.fromkeys("holahola", 1)
print("\nSecuencia con texto y valor: ", name_dic)

#secuencia con texto y lista
name_dic = {}.fromkeys("hola", [1, 2, "Hola"])
print("\nSecuencia con texto y lista: ", name_dic)

#secuencia con texto y diccionario
name_dic = {}.fromkeys("hola", {"Juan": 25, "Maria": 22})
print("\nSecuencia con texto y diccionario: ", name_dic)
