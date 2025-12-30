numeros = [1, 2, 3, 4, 5]
print(f"Lista numeros: {numeros}")
print(f"Lista numeros: {numeros[1:-1]}")
print(f"Lista numeros eliminados: [{numeros[0]}, {numeros[-1]}]\n")

numeros = [1, 2, 3, 4, 5]
print(f"Lista numeros: {numeros}")

numeros_eliminados = []
numeros_eliminados.append(numeros.pop(0))
numeros_eliminados.append(numeros.pop())

print(f"Lista numeros: {numeros} \nLista numeros eliminados: {numeros_eliminados}")