numero = int(input("Que tabla de multiplicar quieres ver?: "))
print(f"Tabla de multiplicar del {numero}")
for indice in range(0, 11) :
    print(f"{numero} x {indice} = {numero * indice}")
