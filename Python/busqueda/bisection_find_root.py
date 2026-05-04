def square_root_bisection(num, tolerance = 0.01, iterations = 50):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if num == 0:
        print('The square root of 0 is 0')
        return 0
    if num == 1:
        print('The square root of 1 is 1')
        return 1

    low = 0 
    high = max(1, num)
    root = None

    for i in range(iterations):
        mid = (low + high) / 2
        square = mid**2

        if (high - low) < tolerance:
            root = mid
            break
        
        if square < num:
            low = mid
        else:
            high = mid
        
    if root is None:
        print(f'Failed to converge within {iterations} iterations')
        return None
    else:
        print(f'The square root of {num} is approximately {root}')
        return root

# square_root_bisection(0)
# square_root_bisection(0.001, 0.0000001, 50)
# square_root_bisection(0.25, 0.0000001, 50)
# square_root_bisection(1)
# square_root_bisection(81, 0.001, 50)
# square_root_bisection(225, 0.001, 100)
# square_root_bisection(225, 0.00001, 100)
# square_root_bisection(225, 0.0000001, 100)
# square_root_bisection(225, 0.0000001, 10)
square_root_bisection(8, 0.001, 50)
