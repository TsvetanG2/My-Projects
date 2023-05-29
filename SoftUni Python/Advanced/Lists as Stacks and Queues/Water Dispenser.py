from collections import deque

people = deque()

water_quantity = int(input())

command = input()
while command != "Start":
    people.append(command)
    command = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        litters_wanted = int(data[0])

        if water_quantity >= litters_wanted:
            water_quantity -= litters_wanted
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(F"{person} must wait")

    else:
        litters_to_fill = int(data[1])
        water_quantity += litters_to_fill
    command = input()\

print(f"{water_quantity} liters left")