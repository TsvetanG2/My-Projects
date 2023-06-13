def rectangle(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Enter valid values!'

    return f'Rectangle area: {a * b}\n'\
           f'Rectangle perimeter: {2 * (a + b)}'


print(rectangle(2, 10))
