import time as t
tiempo_inicio = t.time()

for i in range(7):
    for j in range(7):
        if i == 1 and j == 0:
            continue
        elif i == 2 and j < 2:
            continue
        elif i == 3 and j < 3:
            continue
        elif i == 4 and j < 4:
            continue
        elif i == 5 and j < 5:
            continue
        elif i == 6 and j < 6:
            continue
        else:
            if j == 6:
                print(f"{i}|{j}", end="")
            else:
                print(f"{i}|{j}", end=" - ")

    print("\n")
tiempo_final = t.time()

tiempo_ejecucion = tiempo_final - tiempo_inicio
print(tiempo_ejecucion)

