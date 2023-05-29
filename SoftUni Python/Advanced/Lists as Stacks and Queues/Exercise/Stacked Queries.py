from collections import deque

numbers = deque() #Присвоява стойнсотта

for i in range(int(input())):
    number_data = [int(x) for x in input().split()]
    #или number_data = map(int, input().split)
    command = number_data[0]

    if command == 1:
        numbers.append(number_data[1])
    elif command == 2:
        if numbers:
            numbers.pop()
    elif command == 3:
        if numbers:
            print(max(numbers))
    elif command == 4:
        if numbers:
            print(min(numbers))

numbers.reverse()

print(*numbers, sep=", ")