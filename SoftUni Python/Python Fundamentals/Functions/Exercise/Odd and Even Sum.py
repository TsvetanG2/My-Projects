def OddAndEven(a):
    even_numbers = 0
    odd_numbers = 0

    for digit in a:
        digit = int(digit)

        if digit % 2 == 0:
            even_numbers += digit

        else:
            odd_numbers += digit

    return f'Odd sum = {odd_numbers}, Even sum = {even_numbers}'


input_number = input()
print(OddAndEven(input_number))


