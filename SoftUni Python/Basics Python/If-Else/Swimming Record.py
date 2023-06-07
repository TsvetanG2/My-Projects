import math

world_rec_sec = float(input())
distance = float(input())
time_in_sec_m = float(input())

total_time_sec = distance * time_in_sec_m
delay = math.floor(distance / 15) * 12.5
total = total_time_sec + delay


if world_rec_sec <= total:
    diff = abs(world_rec_sec - total)
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total:.2f} seconds.')