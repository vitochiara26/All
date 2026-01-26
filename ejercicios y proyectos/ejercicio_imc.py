"""El imc resulta de la division de la masa en kg entre el cuadrado de la estatura en metros,
imc < 16 = ingreso, 16 < imc < 16.9 = infrapeso, 17 < imc < 18.4 = bajo peso,
18.5 < imc < 24.9 = peso normal, 25 < imc 29.9 = sobrepeso, 30 < imc < 34.9 = obesidad permorbida,
35 < imc < 45 = obesidad morbida, imc > 45 = obesidad hipermorbida"""

'''Dado el peso en lb (1lb = 0.453592kg) y su estatura en cm. Calcule la salida del peso en kg y m y su imc'''
#Manejo de errores para evitar 
try: 
    peso_usuario = float(input("Ingrese su peso en libras: "))
    estatura_usuario = float(input("Ingrese su estatura en cm: "))
except ValueError:
    print("Ingrese un valor valido")
    exit()

if peso_usuario < 4.7 or peso_usuario > 1400 :
    print("Ingrese un valor de peso en libras mayor a 4.7lb y menor a 1400lb")
    exit()
if estatura_usuario < 25 or estatura_usuario > 300 :
    print("Ingrese un valor de estatura mayor a 55cm y menor a 300cm")
    exit()

peso_usuario *= 0.453592
estatura_usuario /= 100

imc = peso_usuario / (estatura_usuario ** 2)

print(f"Peso: {peso_usuario} | Estatura: {estatura_usuario} | IMC: {imc}")

if imc < 16:
    print("IMC Critico, ingresar a cuidados intensivos")

elif 16 <= imc <= 16.9 :
    print("IMC infrapeso")

elif 17 <= imc <= 18.4 :
    print("IMC bajo peso")

elif 18.5 <= imc <= 24.9 :
    print("IMC peso normal")

elif 25 <= imc <= 29.9:
    print("IMC sobrepeso")

elif 30 <= imc <= 34.9:
    print("IMC obesidad premorbida")

elif 35 <= imc <= 45 :
    print("IMC obesidad morbida")

else :
    print("IMC Obesidad hipermorbida")
