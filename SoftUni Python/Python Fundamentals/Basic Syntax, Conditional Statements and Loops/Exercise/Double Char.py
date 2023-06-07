while True:
    word = input()

    if word == "End":
        break

    repeated_word = False

    if word == "SoftUni":
        repeated_word = True
        continue

    for ch in word:
        print(f'{ch}{ch}', end='')

    print()
