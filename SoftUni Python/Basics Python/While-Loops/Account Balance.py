sum = 0

while True:
    number = input()

    if number == "NoMoreMoney":
        break

    number = float(number)

    if number >= 0:
        sum += number
        print(f"Increase: {number:.2f}")
    else:
        print('Invalid operation!')
        break

print(f'Total: {sum:.2f}')