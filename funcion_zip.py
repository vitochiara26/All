'''Funcion zip para combinar elementos'''
names = ("Luis", "Diego", "Andres", "Carlos")
ages = (15, 30, 26, 12, 40)
text = "Geekiepedia"

print(names)
print(ages)
print(text)

print("\nFuncion zip() como iterable: \n")
combination = zip(names, ages, text)
print(combination)

print("\nFuncion zip() con la funcion list(): \n")
combination = list(zip(names, ages, text))
print(combination)

print("\nFuncion zip() con la funcion tuple(): \n")
combination = tuple(zip(names, ages, text))
print(combination)

print("\nFuncion zip() con for: \n")

for name, age, s_text in zip(names, ages, text):
    print(name, age, s_text)
