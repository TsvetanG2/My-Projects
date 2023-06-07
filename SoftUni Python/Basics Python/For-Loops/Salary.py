count_tabs = int(input())
salary = int(input())

price_of_tab = 0

for i in range (1, count_tabs + 1):
    name_tabs = input()

    if name_tabs == "Facebook":
        price_of_tab += 150
    if name_tabs == "Instagram":
        price_of_tab += 100
    if name_tabs == "Reddit":
        price_of_tab += 50
    if salary <= 0:
        break;

salary -= price_of_tab

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)



