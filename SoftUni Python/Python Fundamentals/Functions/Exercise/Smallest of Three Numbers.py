def get_min_number(numbers):
    return min(numbers)

    #Вариант 2:
    #min_number = float('inf')

    #for num in numbers:
        #if num < min_number:
           # min_number = num

    #return min_number

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(get_min_number([n1, n2, n3]))
