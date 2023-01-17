order = int(input())
total_price = 0

for i in range(order):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 1 <= days <= 31 and 0.01 <= price_per_capsule <= 100 and 1 <= capsules_per_day <= 2000:
        result = price_per_capsule * days * capsules_per_day
        total_price += result

        print(f"The price for the coffee is: ${result:.2f}")

print(f"Total: ${total_price:.2f}")
