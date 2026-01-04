'''Modificacion de una tupla'''
nums_tuple = (5, 8, 3, 3, 1, 6, 2)
print(f"Tupla original: {nums_tuple}\n")

num0 = int(input("Cual de estos numeros quieres modificar por 0?: "))

mod_list = []

for num in nums_tuple:
    if num == num0:
        mod_list.append(0)
    else:
        mod_list.append(num)

mod_tuple = tuple(mod_list)
print(f"\nTupla modificada: {mod_tuple}")


nums_tuple = (5, 8, 3, 3, 1, 6, 2)
print(f"\nTupla original: {nums_tuple}\n")

num = int(input("Cual de estos numeros quieres modificar por 0?: "))
nums_tuple = list(nums_tuple)
len_tuple = len(nums_tuple)

for index in range(len_tuple):
    if nums_tuple[index] == num:
        nums_tuple[index] = 0

nums_tuple = tuple(nums_tuple)
print(f"\nTupla modificada: {nums_tuple}")
