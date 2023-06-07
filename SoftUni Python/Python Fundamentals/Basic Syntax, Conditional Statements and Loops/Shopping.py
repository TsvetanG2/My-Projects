budget = float(input())
command = input()

while command != "End":
    product_price = float(command)
    budget -= product_price
    if budget < 0:
        print(f'You went in overdraft!')
        break
    command = input()

if command == "End":
    print("You bought everything needed.")