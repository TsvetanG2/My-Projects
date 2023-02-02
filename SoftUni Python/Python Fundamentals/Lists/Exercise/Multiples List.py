factor = int(input())
count = int(input())

result = []

for number in range(1, count + 1):
    result.append(number * factor)

print(result)