def multiplicador(factor):
    def funcion_interna(numero):
        return numero * factor
    return funcion_interna


multiplicar_por_2 = multiplicador(2)
multiplicar_por_5 = multiplicador(5)

print(multiplicar_por_2(4))
print(multiplicar_por_5(6))
