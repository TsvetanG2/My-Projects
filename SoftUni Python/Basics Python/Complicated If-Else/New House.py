type_of_flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if type_of_flowers == "Roses":
    price = 5
    if flowers_count > 80:
        price = price * 0.90
elif type_of_flowers == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        price = price * 0.85
elif type_of_flowers == "Tulips":
    price = 2.80
    if flowers_count > 80:
        price = price * 0.85
elif type_of_flowers == "Narcissus":
    price = 3
    if flowers_count < 120:
        price = price * 1.15
elif type_of_flowers == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        price = price * 1.20
flowers_cost = flowers_count * price

if budget >= flowers_cost:
    money_left = budget - flowers_cost
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {money_left:.2f} leva left.")
else:
    money_needed = flowers_cost - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")