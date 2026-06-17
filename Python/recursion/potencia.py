def potencia(n, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return potencia(n*n, k/2)
    else :
        return n * potencia(n, k-1)
    

print(potencia(0, 0))