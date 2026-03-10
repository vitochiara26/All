def calcular_dias_totales(mes_inicial, mes_final, dias_meses, año_fechas):
        bisiesto = sera_bisiesto(año_fechas)
        dias_meses[1] = 28
        if bisiesto:
            dias_meses[1] = 29
        dias_mes_totales = sum(dias_meses[mes_inicial: (mes_final + 1)])
        return dias_mes_totales


def restar_dias_iniciales_y_finales(dia_inicial, dia_final, dias_mes_totales, mes_final, dias_meses, año_fechas):
        dias_sobrantes_inicio = dia_inicial -1
        bisiesto = sera_bisiesto(año_fechas)
        dias_meses[1] = 28
        if bisiesto:
            dias_meses[1] = 29
        dias_sobrantes_final = dias_meses[mes_final] - dia_final
        dias_pasados_exactos = dias_mes_totales - (dias_sobrantes_inicio + dias_sobrantes_final)
        return dias_pasados_exactos

def sera_bisiesto(año_fechas):
    bisiesto = False
    if año_fechas % 4 == 0 :
        if año_fechas % 100 == 0 :
            if año_fechas % 400 == 0 :
                bisiesto = True
            else :
                bisiesto = False
        else :
            bisiesto = True
    else :
        bisiesto = False
    return bisiesto

def unico_salto_de_año(dia_primera_fecha, dia_segunda_fecha, mes_inicial, mes_final, dias_meses, año_primera_fecha, año_segunda_fecha):
        bisiesto = sera_bisiesto(año_primera_fecha)
        if bisiesto:
            dias_meses[1] = 29
        dias_pasados_primera_fecha = sum(dias_meses[mes_inicial: 12])
        dias_pasados_primera_fecha -= dia_primera_fecha

        dias_meses[1] = 28
        bisiesto = sera_bisiesto(año_segunda_fecha)
        if bisiesto:
            dias_meses[1] = 29
        dias_pasados_segunda_fecha = sum(dias_meses[0: (mes_final + 1)])
        dias_pasados_segunda_fecha -= dias_meses[mes_final] - dia_segunda_fecha

        dias_totales_pasados = dias_pasados_primera_fecha + dias_pasados_segunda_fecha
        return dias_totales_pasados

def cuantos_bisiestos(año_primera_fecha, año_segunda_fecha):
    contador_bisiestos = 0
    for año in range (año_primera_fecha, año_segunda_fecha):
        if año % 4 == 0 :
            if año % 100 == 0 :
                if año % 400 == 0 :
                    contador_bisiestos += 1
                else :
                    pass
            else :
                contador_bisiestos += 1
        else :
            pass
    return contador_bisiestos

def unico_salto_de_año(dia_primera_fecha, dia_segunda_fecha, mes_inicial, mes_final, dias_meses, año_primera_fecha, año_segunda_fecha):
        bisiesto = sera_bisiesto(año_primera_fecha)
        if bisiesto:
            dias_meses[1] = 29
        dias_pasados_primera_fecha = sum(dias_meses[mes_inicial: 12])
        dias_pasados_primera_fecha -= dia_primera_fecha

        dias_meses[1] = 28
        bisiesto = sera_bisiesto(año_segunda_fecha)
        if bisiesto:
            dias_meses[1] = 29
        dias_pasados_segunda_fecha = sum(dias_meses[0: (mes_final + 1)])
        dias_pasados_segunda_fecha -= dias_meses[mes_final] - dia_segunda_fecha

        dias_totales_pasados = dias_pasados_primera_fecha + dias_pasados_segunda_fecha
        
        dias_bisiestos = cuantos_bisiestos(año_primera_fecha, año_segunda_fecha)
        diferencial_años = (año_segunda_fecha - año_primera_fecha) - 1 
        dias_totales_pasados += (diferencial_años * 365) + dias_bisiestos 
        return dias_totales_pasados
