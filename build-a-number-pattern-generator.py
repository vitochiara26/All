def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    pattern = ""
    for number in range(1, n + 1):
        pattern += str(number) + " "
    print(pattern.strip())

number_pattern(4)
number_pattern(12)
