a = int(input())

evensum = 0
oddsum = 0

for i in range(a):
    if i % 2 == 0:
        evensum += int(input())
    else:
        oddsum += int(input())
if evensum == oddsum:
    evensum = oddsum
    print(f'Yes')
    print(f'Sum = {evensum}')
else:
    print(f'No')
    print(f'Diff = {abs(evensum - oddsum)}')