import math

average_speed = float(input())
litres_per_100km = float(input())

trip_km = 384_400 * 2


total_time = (math.ceil(trip_km / average_speed)) + 3
total_fuel = (litres_per_100km * trip_km) / 100

print(total_time)
print(int(total_fuel))