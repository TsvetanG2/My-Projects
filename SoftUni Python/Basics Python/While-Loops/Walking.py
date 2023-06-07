sum_steps = 0
goal_for_the_day = 10000
input_line = input()
while input_line != "Going home":
    steps = int(input_line)

    sum_steps += steps

    if sum_steps >= goal_for_the_day:
        break

    input_line = input()

if input_line == "Going home":
    home_steps = int(input())
    sum_steps += home_steps

diff = abs(sum_steps - goal_for_the_day)

if sum_steps >= goal_for_the_day:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f"{diff} more steps to reach goal.")