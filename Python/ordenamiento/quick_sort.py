def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    less_than_pivot = [x for x in array if x < pivot]
    equal_to_pivot = [x for x in array if x == pivot]
    greater_than_pivot = [x for x in array if x > pivot]
    
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
print(quick_sort([]))
