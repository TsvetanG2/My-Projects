squares = float(input())
SquarePrice = 7.61
Result = squares * SquarePrice
Discounted = Result * 0.18
DiscountedPrice = Result - Discounted

print(f'The final price is: {DiscountedPrice} lv.')
print(f'The discount is: {Discounted} lv.')