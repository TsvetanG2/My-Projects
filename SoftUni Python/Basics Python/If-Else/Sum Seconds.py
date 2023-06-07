import math

a = int(input())
c = int(input())
d = int(input())

total_time = a + c + d

minutes = total_time // 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')

