'''Algoritmo que toma la hora exacta y te diga cuantos segundos son en total'''
HORA_VALIDA, MINUTOS_VALIDO, SEGUNDOS_VALIDO, MERIDIAN_VALIDO = False, False, False, False
segundos_totales = 0

hora = int(input("Ingrese la hora actual: "))
if 0 < hora <= 12 :
    HORA_VALIDA = True

minutos = int(input("Ingrese los minutos actuales: "))
if 0 <= minutos <= 59 :
    MINUTOS_VALIDO = True

segundos = int(input("Ingrese los segundos actuales: "))
if 0 <= segundos <= 59 :
    SEGUNDOS_VALIDO = True

meridian = input("Ingrese el meridiano, ¿am o pm?: ").lower()
if meridian in ("am", "pm") :
    MERIDIAN_VALIDO = True


if HORA_VALIDA and MINUTOS_VALIDO and SEGUNDOS_VALIDO and MERIDIAN_VALIDO :
    if meridian in "am" :
        segundos_totales += hora * 3600
        segundos_totales += minutos * 60
        segundos_totales += segundos
        print("La cantidad de segundos que han transcurrido en "
            f"este dia hasta la hora actual son: {segundos_totales}seg")
        segundos_totales = 0

    if meridian in "pm" :
        segundos_totales += 12 * 3600
        segundos_totales += hora * 3600
        segundos_totales += minutos * 60
        segundos_totales += segundos
        print("La cantidad de segundos que han transcurrido en "
            f"este dia hasta la hora actual son: {segundos_totales}seg")
else :
    print("No ingresastes datos validos en algun formato de hora, minuto, segundo o meridiano")
