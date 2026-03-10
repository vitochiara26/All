matriz_a = [[4,2],[1,2],[6,-1],[3,5]]
cambio = []
print("Original",matriz_a)

for i in range(0,len(matriz_a),2):
    cambio = matriz_a[i]
    matriz_a[i] = matriz_a[i+1]
    matriz_a[i+1] = cambio

print("Modificada",matriz_a)
