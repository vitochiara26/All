# **kwargs
def imprimir_info(**info):
    print(info)
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


imprimir_info(nombre= "Victor", edad=26, ciudad="Bejuma")
