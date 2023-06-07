rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
position = None

for row_index in range(rows):
    if position:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_symbol:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f'{searched_symbol} does not occur in the matrix')
