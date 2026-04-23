archivo = open(r'all\Python\archivo\password.txt', 'r', encoding='utf-8')
contraseña_usuario = archivo.read()
archivo.close()

while True:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña_usuario:
        print("Sesion iniciada")
        break
    else: 
        print("Contraseña incorrecta")

nueva_contraseña = input("Ingrese su nueva contraseña: ")

archivo = open(r'all\Python\archivo\password.txt', 'w', encoding='utf-8')
archivo.write(nueva_contraseña)
archivo.close()
