'''Manejo de errores con excepciones'''
try:
    numero = int(input("Ingresa un numero: "))
    resultado = 50 // numero
    print(f"50 / {numero} =", resultado)
except ZeroDivisionError as zde:
    print(f"No se puede dividir entre cero: Error! {zde}")
except ValueError as ve:
    print(f"Debes ingresar un numero entero: Error! {ve}")
except Exception as e:
    print(f"Operacion no valida: {e}")
else:
    print("Operacion exitosa!!!")
finally:
    print("Fin del programa.")
