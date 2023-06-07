rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

diagonal = 0
for index in range(rows):
    diagonal += matrix[index][index]

print(diagonal)
