def fibonacci_sequence(start_sequence, length):
    array = []
    array.append(start_sequence[0])
    array.append(start_sequence[1])
    index = 0
    while len(array) < length:
        result = array[index] + array[index+1]
        array.append(result)
        index += 1
    return array[:length]        
        
    
print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))

