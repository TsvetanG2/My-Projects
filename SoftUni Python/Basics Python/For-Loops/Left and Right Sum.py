import math

a = int(input())

leftsum = 0
rightsum = 0

for i in range(a):
    leftsum += int(input())
for i in range(a):
    rightsum += int(input())
if leftsum == rightsum:
    print(f'Yes, sum = {leftsum}')
else:
    rightsum -= leftsum
    print(f'No, diff = {abs(rightsum)}')