def is_valid_number(n:str, base:int) -> bool:
    validation = True
    check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(check_list[:base])
    for x in n:
        if not x.upper() in check_list[:base]:
            validation = False

    return validation

print(is_valid_number("10101", 16))