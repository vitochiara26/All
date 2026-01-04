'''Crear una tienda virtual'''
print("Bienvenido a la Tienda Virtual")
salir = False
carrito = []
products = {'Camiseta': 20,
            'Jeans': 40,
            'Zapatos': 60,
            'Sombrero': 10
            }


while salir is False:
    print("\nMenú:\n1. Agregar productos al carrito\n2. Ver carrito\n3. Realizar el pago y salir")
    opcion = input("Seleccione una opcion: ")
    if not opcion in ('1', '2', '3'):
        print("Opcion no valida. Por favor, seleccione una opcion valida.")
        continue
    elif opcion == '1':
        print("\nProductos disponibles:")
        [print(f"● {product} ${price}") for product, price in products.items()]
        add_product = input("Ingrese el nombre que desea agregar: ").capitalize()

        if add_product in products:
            carrito.append(add_product)
            print(f"{add_product} agregado al carrito")

    elif opcion == '2':
        print("\nCarrito:")
        for product in set(carrito):
            cantidad = carrito.count(product)
            precio_unidad = products[product]
            print(f"{cantidad} {product} - ${precio_unidad} c/u")

    elif opcion == '3':
        total_pagar = sum(products[product] for product in carrito)
        print(f"Total a pagar: ${total_pagar}")

        try:
            total_pagado = int(input("Ingrese el monto con el que pagará: "))
        except ValueError:
            print("Monto invalido. Por favor, ingrese un monto valido.")

        if total_pagado < total_pagar:
            print("El monto pagado es insuficiente. Por favor, ingrese un monto válido.")
        elif total_pagado == total_pagar:
            print("Gracias por su compra. ¡Exacto! No se requiere cambio.")
            salir = True
        else:
            print(f"Gracias por su compra. Su cambio es: ${total_pagado - total_pagar}")
            salir = True
