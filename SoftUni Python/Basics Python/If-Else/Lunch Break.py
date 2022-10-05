import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch = break_duration / 8
fast_break = break_duration / 4

total = break_duration - lunch - fast_break

diff = abs(total - episode_duration)
rounded_diff = math.ceil(diff)

if total >= episode_duration:
    print(f'You have enough time to watch {series_name} and left with {rounded_diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {rounded_diff} more minutes.")