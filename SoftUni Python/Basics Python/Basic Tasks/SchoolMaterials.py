SumOfPens = int(input()) * 5.80
SumOfPens2 = int(input()) * 7.20
BoardLitres = int(input()) * 1.20
Discount = int(input()) * 0.01

Result = SumOfPens + SumOfPens2 + BoardLitres
Result2 = Result - (Result * Discount)

print(Result2)
