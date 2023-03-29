#Card Check
def is_card_in_the_deck(cards_deck: list, card_name: str):
    if card_name in cards_deck:
        return True

    return False


#Card Index
def card_index(cards_deck: list, index_of_card: str):
    if 0 <= index_of_card < len(cards_deck):
        return True

    return False


#Add Card
def add_card(cards_deck: list, card_name: str):
    if is_card_in_the_deck(cards_deck, card_name):
        print(f'Card is already in the deck')
        return cards_deck

    cards_deck.append(card_name)
    print(f'Card successfully added')
    return cards_deck


#Remove card
def remove_card(cards_deck: list, card_name: str):
    if not is_card_in_the_deck(cards_deck, card_name):
        print(f'Card not found')
        return cards_deck

    cards_deck.remove(card_name)
    print(f'Card successfully removed')
    return cards_deck


#Removes the card at specific position
def remove_card_at(cards_deck: list, cards_position: int):
    if not card_index(cards_deck, cards_position):
        print(f'Index out of range')
        return cards_deck

    cards_deck.pop(cards_position)
    print(f'Card successfully removed')
    return cards_deck


#Insert the card at specific position
def insert_card(cards_deck: list, cards_position: int, cards_name: str):
    if not card_index(cards_deck, cards_position):
        print('Index out of range')
        return cards_deck

    if is_card_in_the_deck(cards_deck, cards_name):
        print('Card is already added')
        return cards_deck

    cards_deck.insert(cards_position, cards_name)
    print('Card successfully added')
    return cards_deck


deck_str = input().split(', ')
commands = int(input())


for i in range(commands):
    command = input().split(', ')
    action = command[0]

    if action == 'Add':
        card = command[1]
        deck_str = add_card(deck_str, card)

    if action == 'Remove':
        card = command[1]
        deck_str = remove_card(deck_str, card)

    if action == 'Remove At':
        index = int(command[1])
        deck_str = remove_card_at(deck_str, index)

    if action == 'Insert':
        index = int(command[1])
        card = command[2]
        deck_str = insert_card(deck_str, index, card)


print(', '.join(deck_str))