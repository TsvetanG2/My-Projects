def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


first = int(input())
second = int(input())
third = int(input())

sum_result = add(first, second)
result = subtract(sum_result, third)

print(result)
