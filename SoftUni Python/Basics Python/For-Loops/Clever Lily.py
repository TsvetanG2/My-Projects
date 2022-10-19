age = int(input())
price_was_machine = float(input())
toy_price = int(input())

brother_count = 0
count_toys = 0
sum_money = 0
money = 0

for i in range(1, age + 1):

    if i % 2 != 0:
        count_toys = count_toys + 1
    else:
        brother_count += 1
        money = money + 10
        sum_money = sum_money + money

result = (count_toys * toy_price) + sum_money - brother_count
diff = abs(result - price_was_machine)

if result >= price_was_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


