n = int(input())

for i in range(1, n + 1):
    is_speacial = False
    i_in_str = str(i)
    sum_digits = 0

    for char in i_in_str:
        sum_digits += int(char)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_speacial = True

    print(f'{i} -> {is_speacial}')