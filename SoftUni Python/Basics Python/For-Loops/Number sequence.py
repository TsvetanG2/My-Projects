import sys

number_of_lines = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for number in range(number_of_lines):
    a = int(input())

    if a > max_number:
        max_number = a
    if a < min_number:
        min_number = a

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
