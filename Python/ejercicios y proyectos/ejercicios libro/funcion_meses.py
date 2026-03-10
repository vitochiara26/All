def calcular_dias(mes_actual):
        total_dias = sum(dias_meses[0:mes_actual])
        print(f"Desde el inicio del año hasta el primer dia del mes de {mes} han pasado {total_dias} dias")


def indice_mes(input_mes):
    if input_mes in meses:
        num_mes = meses.index(input_mes)
        return num_mes
    else :
        print("O escribio mal el nombre del mes o metio algo que no era, de todas maneras intentelo de nuevo dejando la estupidez a un lado")


print("Sistema para calcular cuantos dias van desde el inicio del año hasta el mes ingresado")

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

mes = input("Ingresa el nombre del mes a seleccionar: ").lower()
indice_mes = indice_mes(mes)
calcular_dias(indice_mes)