number = int(input())
sum = 0

while sum != number:
    data = int(input())
    sum += data

    if sum >= number:
        print(sum)
        break