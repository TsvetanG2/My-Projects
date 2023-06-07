rows, cols = [int(el) for el in input().split(', ')]

matrix = []
max_sum = float('-inf')
sub_matrix = []

for i in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    matrix.append(inner_list)

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_element = matrix[row_index][col_index]
        element_below = matrix[row_index+1][col_index]
        next_element = matrix[row_index][col_index+1]
        diagonal_element = matrix[row_index+1][col_index+1]

        sum_elements = current_element + element_below + next_element + diagonal_element

        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[sum_elements, next_element], [element_below, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
