from turtle import *

speed(11)
color('cyan')
bgcolor('black')
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b += 1

    if b == 200:
        input("To end the program input anything")

