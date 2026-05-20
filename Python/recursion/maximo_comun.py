def maximo_comun_divisor(a,b):
    if a > b:
        return maximo_comun_divisor(a-b, b)
    elif a < b: 
        return maximo_comun_divisor(a, b-a)
    else: # a == B
        return a

print(maximo_comun_divisor(24, 36))