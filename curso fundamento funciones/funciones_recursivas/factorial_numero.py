# 5! = 5 x 4 x 3 x 2 x 1 = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n - 1)


resultado_factorial = factorial(5)
print(resultado_factorial)