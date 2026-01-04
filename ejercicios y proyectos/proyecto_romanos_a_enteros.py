try:
    valores_romanos = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000
                       }
    numero_entero = 0
    valor_anterior = 0

    numero_romano = input("Ingresa un numero romano para traducirlo a entero: ").upper()
    numero_romano = numero_romano[::-1]

    for letra in numero_romano:
        valor_actual = valores_romanos[letra]
        print(f"Numero entero: {numero_entero}")
        print(f"Valor actual: {valor_actual}")
        print(f"Valor anterior: {valor_anterior}\n")
        
        if valor_actual < valor_anterior:
            numero_entero -= valor_actual
        else:
            numero_entero += valor_actual
        valor_anterior = valor_actual

    print(numero_entero)

except Exception as e:
    print("Ingresa un numero romano valido", e)
