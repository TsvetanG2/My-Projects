days_of_accommodation = int(input())
type_of_room = input()
rating = input()
room_cost = 0
if type_of_room == "room for one person":
    room_cost = 18
elif type_of_room == "apartment":
    room_cost = 25
    if days_of_accommodation < 10:
        room_cost = 25 * 0.7
    elif 10 <= days_of_accommodation <= 15:
        room_cost = 25 * 0.65
    elif days_of_accommodation > 15:
        room_cost = 25 * 0.5
elif type_of_room == "president apartment":
    room_cost = 35
    if days_of_accommodation < 10:
        room_cost = 35 * 0.9
    elif 10 <= days_of_accommodation <= 15:
        room_cost = 35 * 0.85
    elif days_of_accommodation > 15:
        room_cost = 35 * 0.8

accommodation_bill = (days_of_accommodation - 1) * room_cost

if rating == "positive":
    accommodation_bill = accommodation_bill * 1.25
elif rating == "negative":
    accommodation_bill = accommodation_bill * 0.9

print(f"{accommodation_bill:.2f}")