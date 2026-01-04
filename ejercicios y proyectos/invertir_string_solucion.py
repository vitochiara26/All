string = input("Introduce un string para invertirlo: ")
string_volteada = ""

for letra in string :
    string_volteada = letra + string_volteada
    
print(string_volteada)
