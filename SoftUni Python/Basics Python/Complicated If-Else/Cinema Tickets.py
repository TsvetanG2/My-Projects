price = 0
day = input()

if day == "Monday" or day == "Tuesday" or day == "Friday":
     price += 12
if day == "Wednesday" or day == "Thursday":
    price += 14
if day == "Saturday" or day == "Sunday":
    price += 16

print(price)