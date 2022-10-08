Budget_of_group = int(input())
season = input()
sum_of_fisherman = int(input())

rent = 0

if season == "Spring":
    rent += 3000
    if sum_of_fisherman <= 6:
        rent -= rent * 0.10
    elif 7 <= sum_of_fisherman <= 11:
        rent -= rent * 0.15
    elif sum_of_fisherman >= 12:
        rent -= rent * 0.25
    if (sum_of_fisherman % 2) == 0:
        rent -= rent * 0.05

elif season == "Summer":
    rent += 4200
    if sum_of_fisherman <= 6:
        rent -= rent * 0.10
    elif 7 <= sum_of_fisherman <= 11:
        rent -= rent * 0.15
    elif sum_of_fisherman >= 12:
        rent -= rent * 0.25
    if (sum_of_fisherman % 2) == 0:
        rent -= rent * 0.05

elif season == "Autumn":
    rent += 4200
    if sum_of_fisherman <= 6:
        rent -= rent * 0.10
    elif 7 <= sum_of_fisherman <= 11:
        rent -= rent * 0.15
    elif sum_of_fisherman >= 12:
        rent -= rent * 0.25

elif season == "Winter":
    rent += 2600
    if sum_of_fisherman <= 6:
        rent -= rent * 0.10
    elif 7 <= sum_of_fisherman <= 11:
        rent -= rent * 0.15
    elif sum_of_fisherman >= 12:
        rent -= rent * 0.25
    if (sum_of_fisherman % 2) == 0:
        rent -= rent * 0.05
else:
    print()

if Budget_of_group <= rent:
    rent -= Budget_of_group
    print(f'Not enough money! You need {rent:.2f} leva.')
else:
    Budget_of_group -= rent
    print(f'Yes! You have {Budget_of_group:.2f} leva left.')
