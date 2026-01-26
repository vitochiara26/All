"""Dado un numero entre 1 y 12, indica el MES"""
try :
    num_mes = int(input("Ingrese un numero entre 1 y 12: "))
except ValueError:
    print("Ingrese solo caracteres numericos")
    exit(0)

MES = ""

match num_mes:
    case 1:
        MES = "Enero"
    case 2:
        MES = "Febrero"
    case 3:
        MES = "Marzo"
    case 4:
        MES = "Abril"
    case 5:
        MES = "Mayo"
    case 6:
        MES = "Junio"
    case 7:
        MES = "Julio"
    case 8:
        MES = "Agosto"
    case 9:
        MES = "Septiembre"
    case 10:
        MES = "Octubre"
    case 11:
        MES = "Noviembre"
    case 12:
        MES = "Diciembre"
    case _:
        print("Numero no valido")

print(f"El MES {num_mes} es {MES}")
