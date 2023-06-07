string = input().split()
shuffle_count = int(input())

for shuffle in range(shuffle_count):
    deck = []
    middle_of_deck = len(string) // 2
    left_part = string[0:middle_of_deck]
    right_part = string[middle_of_deck::]

    for card in range(len(left_part)):
        deck.append(left_part[card])
        deck.append(right_part[card])

    string = deck

print(string)