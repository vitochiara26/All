string = "Menu"

print("Metodos con espacios:")
print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))

print("\nMetodos con carater:")
print(string.center(20, "="))
print(string.rjust(20, "="))
print(string.ljust(20, "="))

print("\nVariable modificada:")
string = string.center(10, "=")
print(string)
