row, col = [int(el) for el in input().split(", ")]

matrix = []
col_sums = []

for _ in range(row):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for col_index in range(col):
    sum_col_elements = 0
    for row_index in range(row):
        sum_col_elements += matrix[row_index][col_index]
    col_sums.append(sum_col_elements)

for col_sum in col_sums:
    print(col_sum)