n = int(input())

for first in range(n):
    for second in range(n):
        for third in range(n):
            result = f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}'
            print(result)