def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [el for el in args[:-1] if int(el) % 2 == 0]
        # Хващаме всичко без последният елемент
    else:
        return [el for el in args[:-1] if int(el) % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
