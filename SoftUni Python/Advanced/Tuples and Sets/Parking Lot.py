n = int(input())
cars = set()

for _ in range(n):
    direction, number = input().split(', ')
    if direction == "IN":
        cars.add(number)
    elif direction == "OUT":
        cars.remove(number)

if cars:
    print(*cars, sep='\n')
else:
    print("Parking Lot is Empty")

