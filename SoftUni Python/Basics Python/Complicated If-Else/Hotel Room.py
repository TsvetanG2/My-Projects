month = input()
days = int(input())
studio_room = 0
apartment_room = 0

if month in " May October ":
    studio_room = 50
    apartment_room = 65
    if 7 < days <= 14:
        studio_room = studio_room * 0.95
    elif 14 < days:
        studio_room = studio_room * 0.70
        apartment_room = apartment_room * 0.90
elif month in " June September ":
    studio_room = 75.20
    apartment_room = 68.70
    if 14 < days:
        studio_room = studio_room * 0.80
        apartment_room = apartment_room * 0.90
elif month in " July August ":
    studio_room = 76
    apartment_room = 77
    if 14 < days:
        apartment_room = apartment_room * 0.90

apartment_cost = apartment_room * days
studio_cost = studio_room * days

print(f'Apartment: {apartment_cost:.2f} lv.')
print(f'Studio: {studio_cost:.2f} lv.')