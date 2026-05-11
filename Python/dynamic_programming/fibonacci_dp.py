def fibonacci(n):
    sequence = [0, 1]
    index_one = 0
    index_two = 1
    if n == 0:
        return sequence[0]
    while len(sequence) <= n:
        sequence.append(sequence[index_one] + sequence[index_two])
        index_one += 1
        index_two += 1
    return sequence[-1]


print(fibonacci(3))