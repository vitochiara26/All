string = input("Introduce un String: ")

print(f"\nTodas las letras estan en minusculas?: {string.islower()}")
string = string.lower()
print(f"String en minusculas: {string}")

print(f"\nTodas las letras estan en mayusculas?: {string.isupper()}")
print(f"String en mayusculas: {string.upper()}")

print(f"Sting original: {string}")
