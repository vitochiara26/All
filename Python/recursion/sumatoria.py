def sumatoria(num):
    if num == 1:
        return 1
    else:
        return num + sumatoria(num - 1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input('Numero de la sumatoria: '))
print(sumatoria(num))

n = int(input('Numero del factorial: '))
print(factorial(n))
