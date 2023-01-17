n = int(input())

for i in range(n):
    string = input()

    pure = True
    for ch in string:
        if ch == "," or ch == "." or ch == "_":
            pure = False
            break

    if pure == True:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')