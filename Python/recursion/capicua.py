def es_capicua(palabra, index_inicial = 0, index_final = -1 ):
    if index_inicial + 1 <= len(palabra) // 2:
        
        if palabra[index_inicial].lower() == palabra[index_final].lower():
            index_inicial += 1
            index_final -= 1
            return es_capicua(palabra, index_inicial, index_final)
        else :
            return False
    return True


palabra_uno = ['a', 'l', 'l', 'a']
palabra_dos = ['s', 'o', 'l', 'o', 's']
palabra_tres =['v', 'i', 'c', 't', 'o', 'r']

print(f'La palabra "{''.join(palabra_uno).capitalize()}" es capicua?: {es_capicua(palabra_uno)}')
print(f'La palabra "{''.join(palabra_dos).capitalize()}" es capicua?: {es_capicua(palabra_dos)}')
print(f'La palabra "{''.join(palabra_tres).capitalize()}" es capicua?: {es_capicua(palabra_tres)}')
