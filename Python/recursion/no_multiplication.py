def multiplication(a, b):
    if b == 0:
        return 0
    
    if b < 0:
        return -multiplication(a, -b)
    
    return a + multiplication(a, b - 1)

print(f"5 x 3 = {multiplication(5, 3)}")       
print(f"10 x 0 = {multiplication(10, 0)}")     
print(f"7 x -2 = {multiplication(7, -2)}")     
print(f"2.5 x 4 = {multiplication(2.5, 4)}")
