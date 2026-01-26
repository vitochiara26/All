'''Somos un concesionario (Bera ;) ) y ofrecemos 5 motos, con 3 accesorios, cada moto y cada accesorio debe tener un precio'''
meru110_2024 = 700
brf_2025 = 1300
sbr_2026 = 1800
br200_2026 = 2300
gbr_2024 = 2700

portaplaca = 5
reposapuño = 1
casco = 10

seleccion = ""

print("Bienvenido a motos bera, c.a.")
presupuesto = float(input("Ingrese su presupuesto para indicarle que moto podria comprar: "))

if presupuesto < meru110_2024:
    print("Su presupuesto no es suficiente para comprar una moto, lo sentimos.")

elif presupuesto >= meru110_2024 and presupuesto < brf_2025 :
    print("Por ese presupuesto puede adquirir una Meru 110cc")
    print("Que viene con los accesorios: Portaplaca, reposapuño y casco sandoval")
    print("Con un precio total de: " , (meru110_2024 + portaplaca + reposapuño + casco))
    seleccion = input("Desear remover los accesarios? Escribe 'si' para removerlos del precio y 'no' : ").lower()
    if seleccion == "si" :
        print("El precio de la moto sin articulos seria: ", meru110_2024)
    elif seleccion== "no" :
        print("El precio de la moto con articulos seria: " , (meru110_2024 + portaplaca + reposapuño + casco))
    else :
        print("Respuesta invalida.")

elif presupuesto >= brf_2025 and presupuesto < sbr_2026 :
    print("Por ese presupuesto puede adquirir una Brf 150cc")
    print("Que viene con los accesorios: Portaplaca, reposapuño y casco sandoval")
    print("Con un precio total de: " , (brf_2025 + portaplaca + reposapuño + casco))
    seleccion = input("Desear remover los accesarios? Escribe 'si' para removerlos del precio y 'no' : ").lower()
    if seleccion == "si" :
        print("El precio de la moto sin articulos seria: ", brf_2025)
    elif seleccion== "no" :
        print("El precio de la moto con articulos seria: " , (brf_2025 + portaplaca + reposapuño + casco))
    else :
        print("Respuesta invalida.")

elif presupuesto >= sbr_2026 and presupuesto < br200_2026 :
    print("Por ese presupuesto puede adquirir una Sbr 150cc")
    print("Que viene con los accesorios: Portaplaca, reposapuño y casco sandoval")
    print("Con un precio total de: " , (sbr_2026 + portaplaca + reposapuño + casco))
    seleccion = input("Desear remover los accesarios? Escribe 'si' para removerlos del precio y 'no' : ").lower()
    if seleccion == "si" :
        print("El precio de la moto sin articulos seria: ", sbr_2026)
    elif seleccion== "no" :
        print("El precio de la moto con articulos seria: " , (sbr_2026 + portaplaca + reposapuño + casco))
    else :
        print("Respuesta invalida.")

elif presupuesto >= br200_2026 and presupuesto < gbr_2024  :
    print("Por ese presupuesto puede adquirir una BR200 200cc")
    print("Que viene con los accesorios: Portaplaca, reposapuño y casco sandoval")
    print("Con un precio total de: " , (br200_2026 + portaplaca + reposapuño + casco))
    seleccion = input("Desear remover los accesarios? Escribe 'si' para removerlos del precio y 'no' : ").lower()
    if seleccion == "si" :
        print("El precio de la moto sin articulos seria: ", br200_2026)
    elif seleccion== "no" :
        print("El precio de la moto con articulos seria: " , (br200_2026 + portaplaca + reposapuño + casco))
    else :
        print("Respuesta invalida.")
    
else :
    print("Por ese presupuesto puede adquirir una Gbr 200cc")
    print("Que viene con los accesorios: Portaplaca, reposapuño y casco sandoval")
    print("Con un precio total de: " , (gbr_2024 + portaplaca + reposapuño + casco))
    seleccion = input("Desear remover los accesarios? Escribe 'si' para removerlos del precio y 'no' : ").lower()
    if seleccion == "si" :
        print("El precio de la moto sin articulos seria: ", gbr_2024)
    elif seleccion== "no" :
        print("El precio de la moto con articulos seria: " , (gbr_2024 + portaplaca + reposapuño + casco))
    else :
        print("Respuesta invalida.")
