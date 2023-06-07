count = int(input())
maxElement = int(input())
sum = maxElement

for i in range(count - 1):
    current = int(input())
    sum += current
    if current > maxElement:
        maxElement = current

sum -= maxElement

if sum == maxElement:
    print(f"Yes")
    print(f'Sum = {sum}')
else:
    print(f"No")
    print(f'Diff = {abs(sum - maxElement)}')