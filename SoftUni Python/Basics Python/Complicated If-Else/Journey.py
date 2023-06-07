budget = float(input())
season = input()

destination = ''
holiday = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == "summer":
        budget *= 0.30
        holiday = "Camp"
    elif season == "winter":
        budget *= 0.70
        holiday = "Hotel"
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        holiday = "Camp"
        budget *= 0.40
    elif season == "winter":
        holiday = "Hotel"
        budget *= 0.80
if budget > 1000:
    destination = 'Europe'
    if season == "summer" or season == "winter":
        holiday = "Hotel"
        budget *= 0.90

print(f'Somewhere in {destination}')
print(f'{holiday} - {budget:.2f}')