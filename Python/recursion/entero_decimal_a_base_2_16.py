def int_to_binary(num):
    base = 2
    if num < base:
        return str(num)
    
    return int_to_binary(num // base) + str(num % base)

def int_to_hex(num):
    base = 16
    hex_digits = "0123456789ABCDEF"
    
    if num < 16:
        return hex_digits[num]
    
    return int_to_hex(num // base) + hex_digits[num % 16]


numero = 37
print(f"Numero: {numero} | Binario: {int_to_binary(numero)}")
print(f"Numero: {numero} | Hexadec: {int_to_hex(numero)}")
