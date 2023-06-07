string = input()
count = int(input())

price = 0

def Order(a, b, c):
    if a == "water":
        c = 1.00
    elif a == "coke":
        c = 1.40
    elif a == "coffee":
        c = 1.50
    elif a == "snacks":
        c = 2.00

    result = b * c
    print(f'{result:.2f}')

Order(string, count, price)