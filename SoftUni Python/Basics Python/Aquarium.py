Lenght = int(input())
Width = int(input())
Height = int(input())
Percent = float(input()) * 0.01

Aquarium = Lenght * Width * Height
TurnIntoLitres = Aquarium * 0.001
LitresNeeded = TurnIntoLitres * (1 - Percent)

print(LitresNeeded)