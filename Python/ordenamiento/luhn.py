def verify_card_number(digits_chain: str):
    acount_number = [x for x in digits_chain if x.isdigit()]
    double_every_other = []
    
    for x in range(-1, -1*(len(acount_number)+1), -1):
        if x % 2 != 0:
            double_every_other.insert(0, int(acount_number[x]))
        else:
            double_num = int(acount_number[x]) * 2
            if double_num > 9:
                double_num = str(double_num)
                sum_2_digits = int(double_num[0]) + int(double_num[1])
                double_every_other.insert(0, sum_2_digits)
            else :
                double_every_other.insert(0, double_num)
    
    validation_sum = sum(double_every_other)
    if validation_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'
    
print(verify_card_number('453914881'))