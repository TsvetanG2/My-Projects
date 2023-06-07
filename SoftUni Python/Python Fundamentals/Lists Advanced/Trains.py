number_wagons = int(input())
train = [0] * number_wagons

#for i in range(number_wagons):
    #train.append(0)

commands = input()

while commands != "End":
    action = commands.split()[0]

    if action == "add":
        number_people = int(commands.split()[1])
        train[-1] += number_people

    elif action == "insert":
        index = int(commands.split()[1])
        number_people = int(commands.split()[2])
        train[index] += number_people

    elif action == "leave":
        index = int(commands.split()[1])
        number_people = int(commands.split()[2])
        train[index] -= number_people

    commands = input()

print(train)
