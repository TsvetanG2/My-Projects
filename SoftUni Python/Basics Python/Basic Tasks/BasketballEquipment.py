YearTax = int(input())

BasketballSneakers = YearTax - (YearTax * 0.40)
BasetballSet = BasketballSneakers - (BasketballSneakers * 0.20)
BasketBALL = BasetballSet / 4
Accessories = BasketBALL / 5

ResultPrice = YearTax + BasketballSneakers + BasetballSet + BasketBALL + Accessories

print(ResultPrice)