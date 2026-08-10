import implementacion_lista as my_li

def palindromo(lista, caracter_incial = 0, caracter_final = -1):
    while caracter_incial < lista.size // 2 :
        if (str(lista.search_node(caracter_incial)).lower() ==
            str(lista.search_node(caracter_final)).lower()):
            return palindromo(lista, caracter_incial + 1, caracter_final -1)
        else :
            return "Los caracateres en la lista no forman un palindromo"
    
    return "Los caracateres en la lista forman un palindromo"

lista_pal = my_li.ListaSencilla()
lista_pal.insert_node('O')
lista_pal.insert_node('S')
lista_pal.insert_node('O')

print(palindromo(lista_pal))
