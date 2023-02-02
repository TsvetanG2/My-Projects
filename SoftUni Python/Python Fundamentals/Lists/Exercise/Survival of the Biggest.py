numbers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    number_to_remove = min(numbers)
    numbers.remove(number_to_remove)

# Вариант 1
print(', '.join([str(x) for x in numbers]))

# Вариант 2
#for idx in range(len(numbers)):
    #num = numbers[idx]
    #if idx == len(numbers) - 1:
       # print(num)
   # else:
        #print(num, end=', ')