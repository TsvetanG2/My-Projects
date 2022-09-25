ChikenMenu = 10.35
FishMenu = 12.40
VegMenu = 8.15
Delivery = 2.50

SumOfChicken = int(input())
SumOfFish = int(input())
SumOfVeg = int(input())

Result = (SumOfChicken * ChikenMenu) + (SumOfFish * FishMenu) + (SumOfVeg * VegMenu)
Desert =  Result * 0.20
Overall = Result + Desert + Delivery

print(Overall)