num1 = int(input())

sum = -100000000000000000

while True:
    data = input()

    if data == "Stop":
        break

    data = int(data)

    if data > sum:
        sum = data

if num1 > sum:
    print(num1)
else:
    print(sum)



