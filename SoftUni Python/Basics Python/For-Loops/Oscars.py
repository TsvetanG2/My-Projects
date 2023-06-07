actors_name = input()
academy_points = float(input())
judge_sum = int(input())

total_points = academy_points

for i in range(1, judge_sum + 1):
    judge_name = input()
    judge_points = float(input())

    current_points = (len(judge_name) * judge_points) / 2
    total_points += current_points

    if total_points >= 1250.5:
        break;

if total_points >= 1250.5:
    print(f'Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!')
else:
    diff = abs(1250.5 - total_points)
    print(f'Sorry, {actors_name} you need {diff:.1f} more!')

