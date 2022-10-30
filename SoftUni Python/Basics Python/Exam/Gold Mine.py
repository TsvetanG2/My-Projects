locations = int(input())



for i in range(1, locations + 1):
    expectedgold = float(input())
    days = int(input())
    goldfortheday = 0

    for j in range(1, days + 1):
        expectedgold2 = float(input())
        goldfortheday += expectedgold2

    average = goldfortheday / days

    if average >= expectedgold:
        print(f'Good job! Average gold per day: {average:.2f}.')
    else:
        diff = abs(average - expectedgold)
        print(f'You need {diff:.2f} gold.')


