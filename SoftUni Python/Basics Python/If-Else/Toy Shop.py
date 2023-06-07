TripPrice = float(input())
PuzzleSum = int(input())
SumDolls = int(input())
SumTeddy = int(input())
SumMinios = int(input())
SumTrucks = int(input())

TotalPrice = (PuzzleSum * 2.60) + (SumDolls * 3) + (SumTeddy * 4.10) + (SumMinios * 8.20) + (SumTrucks * 2)

ToyTotal = PuzzleSum + SumDolls + SumTeddy + SumMinios + SumTrucks

if ToyTotal > 50:
    Discount = TotalPrice * 0.25
else:
    Discount = 0

TotalPrice = TotalPrice - Discount

Rent = TotalPrice * 0.10

PriceAfterRent = TotalPrice - Rent

if PriceAfterRent > TripPrice:
    PriceAfterRent -= TripPrice
    print(f'Yes! {PriceAfterRent:.2f} lv left.')
else:
    TripPrice -= PriceAfterRent
    print(f'Not enough money! {TripPrice:.2f} lv needed.')
