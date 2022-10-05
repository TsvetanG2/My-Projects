FilmBudget = float(input())
ActorsSum = int(input())
DressPriceForEach = float(input())

DressTotal = ActorsSum * DressPriceForEach
Decor = FilmBudget * 0.10

if ActorsSum > 150:
    DressTotal -= DressTotal * 0.1

TotalPrice = DressTotal + Decor

diff = abs(FilmBudget - TotalPrice)
if FilmBudget >= TotalPrice:
    print("Action!")
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print("Not enough money!")
    print(f'Wingard needs {diff:.2f} leva more.')