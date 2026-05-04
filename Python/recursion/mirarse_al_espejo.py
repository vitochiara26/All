def mirarse_al_espejo():
    print('me miro al espejo y veo que...')
    mirarse_al_espejo()

# mirarse_al_espejo()

def contar_desde_hasta(m, n):
    if m <= n: 
        print(m)
        m += 1
        contar_desde_hasta(m, n)
    else: 
        print('Fin.')
        

contar_desde_hasta(10, 20)
contar_desde_hasta(0, 10)
