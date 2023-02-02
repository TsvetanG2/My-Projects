gifts = input().split(' ')

command = input().split(' ')
while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]

        while gift in gifts:
            index = gifts.index(gift)
            gifts[index] = 'None'

    elif command[0] == 'Required':
        try:
            index = int(command[2])
            if len(gifts) > index >= 0:
                gifts[index] = command[1]

        except IndexError:
            pass

    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

    command = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')

for i in gifts:
    print(i, end=' ')