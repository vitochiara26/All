longitud = int(input("Cuantos numeros enteros contendrá la lista?: "))
vuelta = 0
lista = []

while vuelta < longitud :
    lista.append(int(input("Introduce un numero entero: ")))
    vuelta += 1

print(f"\nLista: {lista} \nLa suma total de los elementos es: {sum(lista)}")