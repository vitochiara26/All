#ejemplo de break
print("While con la sentencia break\n")
contador = 0
while contador < 10 :
    contador += 1

    if contador == 5 :
        print("Fin del programa, la sentencia break se ha ejecutado.")
        break
    
    print("Valor actual de la variable:", contador)

#ejemplo de continue
print("\nWhile con la sentencia continue\n")
contador = 0
while contador < 10 :
    contador += 1

    if contador == 5 :
        continue
    
    print("Valor actual de la variable:", contador)
