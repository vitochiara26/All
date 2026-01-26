"""Convertir una cantidad de segundos, suministrados como un valor
entero positivo, a minutos y a horas"""
seg = 352846
print(f"{seg} segundos serian equivalentes a {seg//60} minutos sobrando {seg % 60} segundo/s")
print(f"{seg} segundos serian equivalentes a {(seg//60)//60} horas sobrando {(seg//60) % 60} minuto/s y {seg % 60} segundo/s")
print(f"{seg} segundos serian equivalentes a {((seg//60)//60)//24} dias {(seg//60)//60} horas sobrando {(seg//60) % 60} minuto/s y {seg % 60} segundo/s")
