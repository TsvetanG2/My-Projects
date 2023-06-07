string_operator = input()
first_number = int(input())
second_number = int(input())

def solve(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result

print(solve(string_operator, first_number, second_number))
