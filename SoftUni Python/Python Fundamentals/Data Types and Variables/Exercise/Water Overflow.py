capacity = 255

n = int(input())
tank = 0
for _ in range(n):
    water_litres = int(input())
    if tank + water_litres > capacity:
        print('Insufficient capacity!')
    else:
        tank += water_litres

print(tank)