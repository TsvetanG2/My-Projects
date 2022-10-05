hour = int(input())
min = int(input())


total = (hour * 60) + min + 15

hours = total // 60
minutes = total % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')