numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):

    #На всеки просяк принадлежи собственият му индекс. Тоест от Input - 1, 2, 3, 4, 5..
    #1 ще е 0, 2 ще е 1. Защото започваме да броим от 0, а не от 1
    beggar_idx = idx % beggars_count
    num = int(numbers[idx])
    beggars[beggar_idx] += num

print(beggars)