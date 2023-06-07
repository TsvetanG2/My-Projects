import math

shape = input()

if shape == 'square':
    a = float(input())
    result = a * a
elif shape == 'rectangle':
    a1 = float(input())
    b = float(input())
    result = a1 * b
elif shape == 'circle':
    a2 = float(input())
    result = math.pi * a2 * a2
elif shape == 'triangle':
    a3 = float(input())
    b3 = float(input())
    result = a3 * b3 / 2

print(f'{result:.3f}')
