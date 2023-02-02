red_cards = input().split()

first_team_sent_off_players = []
second_team_sent_off_players = []

Is_terminated = False
team_capacity = 11

for card in red_cards:

    if card in first_team_sent_off_players or card in second_team_sent_off_players:
        continue

    card_args = card.split("-")
    team_name = card_args[0]
    player_number = card_args[1]

    is_first_team = team_name == 'A'
    if is_first_team:
        first_team_sent_off_players.append(card)
    else:
        second_team_sent_off_players.append(card)

    if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
        Is_terminated = True
        break

print(f'Team A - {team_capacity - len(first_team_sent_off_players)};'
      f' Team B - {team_capacity - len(second_team_sent_off_players)}')

if Is_terminated:
    print('Game was terminated')