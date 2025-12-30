'''El metodo clear en diccionarios'''
employees = {"Juan": {"edad": 28, "Salario": 25000},
             "Maria": {"edad": 24, "Salario": 20000}
             }

print(f"Diccionario original: {employees}")

employees.clear()

print(f"Diccionario actualizado: {employees}")
