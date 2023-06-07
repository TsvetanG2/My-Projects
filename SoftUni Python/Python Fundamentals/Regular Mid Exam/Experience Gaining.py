experience_needed = float(input())
battles_amount = int(input())
experience_collected = 0

Is_experience_collected = False

for i in range(1, battles_amount + 1):
    experience_earned_per_battle = float(input())
    experience_collected += experience_earned_per_battle

    if i % 3 == 0:
        experience_collected += experience_earned_per_battle * 0.15
    if i % 5 == 0:
        experience_collected -= experience_earned_per_battle * 0.10

    if experience_collected >= experience_needed:
        print(f'Player successfully collected his needed experience for {i} battles.')
        Is_experience_collected = True
        break

if not Is_experience_collected:
    experience_needed -= experience_collected
    print(f'Player was not able to collect the needed experience, {abs(experience_needed):.2f} more needed.')
