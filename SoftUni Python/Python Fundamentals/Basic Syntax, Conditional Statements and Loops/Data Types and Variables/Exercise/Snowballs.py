n = int(input())

best_snowball = float('-inf')
output = ''
for idx in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality

    if result > best_snowball:
        best_snowball = result
        output = f'{weight} : {time} = {best_snowball} ({quality})'

print(output)