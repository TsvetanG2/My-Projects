items_with_their_prices = input().split("|")
budget = float(input())
bought_items_prices = []
profit = 0.0

for ls in items_with_their_prices:
    item_price = ls.split("->")
    item = item_price[0]
    price = float(item_price[1])

    if budget >= price and (item == "Clothes" and price <= 50.0 or
                            item == "Shoes" and price <= 35.0 or
                            item == "Accessories" and price <= 20.50):
        bought_items_prices.append(price * 1.4)
        budget -= price
        profit += price * 0.4

print(" ".join([str(f"{x:.2f}") for x in bought_items_prices]))
print(f"Profit: {profit:.2f}")

if budget + sum(bought_items_prices) >= 150.0:
    print("Hello, France!")
else:
    print("Not enough money.")