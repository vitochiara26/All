print("*Sistema para calcular dias de Vacaciones.*\n")

nombre = input("Introduce tu nombre: ")
clave = int(input("Intoduce tu clave [1 = Atencion al cliente; 2 = Logistica; 3 = Gerencia;]: "))
años = int(input("Introduce la cantidad de años que tienes trabajando en esta empresa: "))


#Flujo para los trabajdaores de atencion al cliente
if clave == 1 :
    clave = str("atencion al cliente")
    if años == 1 :
        dias_vacaciones = 6
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tu año de servicio en esta empresa.\n")
        
    elif años >= 2 and años <= 6 :
        dias_vacaciones = 14
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

    elif años >= 7 :
        dias_vacaciones = 20
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

    else :
        print(nombre , " aun no gozaras del derecho a vacaciones.\n")
        
        
#Flujo para los trabajadores de logistica       
elif clave == 2 :
     clave = str("logistica")
     if años == 1 :
        dias_vacaciones = 7
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tu año de servicio en esta empresa.\n")
        
     elif años >= 2 and años <= 6 :
        dias_vacaciones = 15
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

     elif años >= 7 :
        dias_vacaciones = 22
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

     else :
        print(nombre , " aun no gozaras del derecho a vacaciones.\n")
        
        
#Flujo para la gerencia         
elif clave == 3 :
     clave = str("gerencia")
     if años == 1 :
        dias_vacaciones = 10
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tu año de servicio en esta empresa.\n")
        
     elif años >= 2 and años <= 6 :
        dias_vacaciones = 20
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

     elif años >= 7 :
        dias_vacaciones = 30
        print("\n" + nombre + ", del departamento de " + clave + ", gozaras de " + str(dias_vacaciones) + " dias de vacaciones debido a tus " + str(años) + " años de servicio en esta empresa.\n")

     else :
        print(nombre , " aun no gozaras del derecho a vacaciones.\n")
    
else :
    print("La clave no existe.")


print("Fin.")
