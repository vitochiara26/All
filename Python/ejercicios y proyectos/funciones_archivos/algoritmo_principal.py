import funciones_creadas as fc

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

primera_fecha = input("Ingrese una fecha incial con el formato d/m/a: ").split("/")
segunda_fecha = input("Ingrese una fecha final con el formato d/m/a: ").split("/")

if primera_fecha[2] == segunda_fecha[2] :
    dias_mes_totales = fc.calcular_dias_totales(int((primera_fecha[1]))-1,int((segunda_fecha[1]))-1,dias_meses, int((segunda_fecha[2])))
    dias_pasados = fc.restar_dias_iniciales_y_finales(int((primera_fecha[0])),int((segunda_fecha[0]))-1,dias_mes_totales, int((segunda_fecha[1]))-1, dias_meses, int((segunda_fecha[2])))
    print(dias_pasados)
elif (int(segunda_fecha[2]) - int(primera_fecha[2])) == 1:
    dias_totales = fc.unico_salto_de_año(int(primera_fecha[0]), int(segunda_fecha[0]), int(primera_fecha[1])-1, int(segunda_fecha[1])-1, dias_meses, int(primera_fecha[2]), int(segunda_fecha[2]))
    print(dias_totales)
else:
    dias_totales = fc.unico_salto_de_año(int(primera_fecha[0]), int(segunda_fecha[0]), int(primera_fecha[1])-1, int(segunda_fecha[1])-1, dias_meses, int(primera_fecha[2]), int(segunda_fecha[2]))
    print(dias_totales)