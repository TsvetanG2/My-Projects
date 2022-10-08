
cinema_type = input()
rows = int(input())
columns = int(input())
income = 0
capacity = rows * columns
if cinema_type == "Premiere":
    income = capacity * 12
elif cinema_type == "Normal":
    income = capacity * 7.50
elif cinema_type == "Discount":
    income = capacity * 5
print(f"{income:.2f}")