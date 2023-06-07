import math

a = float(input())
b = float(input())
c = float(input())
heigth_of_the_astronaut = float(input())

spaceship_volume = a * b * c
room_volume = (heigth_of_the_astronaut + 0.40) * 2 * 2
space_for_astronauts = spaceship_volume / room_volume
astronauts_sum = math.floor(space_for_astronauts)

if astronauts_sum >= 3 and astronauts_sum <= 10:
    print(f'The spacecraft holds {astronauts_sum} astronauts.')

elif astronauts_sum < 3:
    print('The spacecraft is too small.')
elif astronauts_sum > 10:
    print('The spacecraft is too big.')

