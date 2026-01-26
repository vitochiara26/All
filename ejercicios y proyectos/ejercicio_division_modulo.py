''''Solicitar un numero de 4 digitos y descomponerlos en unidades , decenas y centenas'''
num = int(input("Ingresa un numero entero de 4 digitos: "))

if num < 1000 or num > 9999:
    print("Eres pendejo o que?")
    
elif num > 1000 or num < 9999: 
    print(str(num // 1000) + " Miles")
    print((num % 1000) // 100 , "Centenas")
    print((num % 100) // 10 , "Decenas")
    if num % 10 == 1 :
        print(num % 10, "Unidad")
    else :
        print(num % 10, "Unidades")
        
        
