def serie_armonica(n):
    if n == 1:
        return 1
    
    return 1 / n + serie_armonica(n - 1)

print(round(serie_armonica(20), 4))