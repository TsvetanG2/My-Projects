start = ord('a')
end = int(input()) + start

for first in range(start, end):
    for second in range(start, end):
        for third in range(start, end):
            result = f'{chr(first)}{chr(second)}{chr(third)}'
            print(result)