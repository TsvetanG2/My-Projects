import math

tournaments_count = int(input())
points = int(input())

total_win_points = 0
win_count = 0

for i in range(1, tournaments_count + 1):
    result = input()

    if result == "W":
        points += 2000
        total_win_points += 2000
        win_count += 1

    elif result == "F":
        points += 1200
        total_win_points += 1200

    elif result == "SF":
        points += 720
        total_win_points += 720

print(f"Final points: {points}")

average = total_win_points / tournaments_count
print(f'Average points: {math.floor(average)}')


percent_win = win_count / tournaments_count * 100
print(f'{percent_win:.2f}%')