"""Calcular el promedio de 4 temperaturas medidas en °C (Celsius) y 
mostrar su equivalente en °F (Fahrenhei)"""

temp_uno = 0 #Congelacion del agua 
temp_dos = 20 #temperatura ambiente
temp_tres = 37 #temperatura corporal
temp_cuatro = 100 #ebullicion del agua

temp_c = (temp_uno + temp_dos + temp_tres + temp_cuatro) / 4
temp_f = (temp_c * 1.8) + 32

print(f"El promedio de las cuatro temperaturas °C en °F: {temp_f}°")