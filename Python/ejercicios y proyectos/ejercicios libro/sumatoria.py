n = int(input("Ingrese el valor i: "))
sumatoria_total = 0
productoria_ciclo_actual = 0
productoria_total_ciclo = 1
for i in range(1, n+1):
    for j in range(1,i+1):
        productoria_ciclo_actual = j**2
        productoria_total_ciclo *= productoria_ciclo_actual
    productoria_ciclo_actual = 0
    sumatoria_total += productoria_total_ciclo
    productoria_total_ciclo = 1
print(sumatoria_total)