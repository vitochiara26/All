"""Calcular pi"""

n_final = int(input("Ingrese en numero total para n: "))
pi = 4
n = 3
operacion = False

while n < n_final:
    if operacion is False:
        div = 4 / n
        if div < 0 :
            div *= -1
        pi -= div
        n += 2
        operacion = True
        print(pi, "\n")

    else :
        div = 4 / n
        if div < 0 :
            div *= -1
        pi += div
        operacion = False
        n += 2
        print(pi, "\n")
