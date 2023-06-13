def func_executor(*funcs):
    result = []

    for func, args in funcs:
        result.append(f"{func.__name__} - {func(*args)}")

    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_nums(num1, num2):
    return num1 * num2

