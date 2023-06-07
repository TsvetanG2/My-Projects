n_lines = int(input())

result = 0

for i in range(n_lines):
    char = input()
    result += ord(char)

print(f'The sum equals: {result}')