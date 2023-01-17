number = int(input())
max_number = int(input())

for num in range(1, max_number + 1):
    if num % number == 0:
        sum = num
        
print(sum)