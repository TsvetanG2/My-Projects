def MinMaxSum(a):
    numbers_min = min(a)
    numbers_max = max(a)
    result = 0

    for digit in a:
        digit = int(digit)
        result += digit

    print(f'The minimum number is {numbers_min}')
    print(f'The maximum number is {numbers_max}')
    print(f'The sum number is: {result}')

    return numbers_min, numbers_max, result


numbers = [int(x) for x in input().split()]
MinMaxSum(numbers)