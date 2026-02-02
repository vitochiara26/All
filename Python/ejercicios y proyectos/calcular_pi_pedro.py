pi = 0
for n in range(0,101):
    pi += ((-1)**n)/(2*n+1)
pi = pi * 4
print(pi)