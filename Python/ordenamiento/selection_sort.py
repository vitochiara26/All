def selection_sort(array):
    for x in range(len(array)):
        lower_position = x

        for y in range(x+1, len(array)):
            if array[y] < array[lower_position]:
                lower_position = y

        if lower_position != x:
            array[x], array[lower_position] = array[lower_position], array[x]

    return array

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))