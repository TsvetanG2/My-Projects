rows, columns = [int(x) for x in input().split(', ')]
matrix = []
largest_sum = 0

for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

position_top_left = 0
position_top_right = 0
position_bottom_left = 0
position_bottom_right = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_sum = matrix[row][column] + matrix[row+1][column] + matrix[row][column+1] + matrix[row+1][column+1]
        if current_sum > largest_sum:
            largest_sum = current_sum
            position_top_left = matrix[row][column]
            position_top_right = matrix[row][column+1]
            position_bottom_left = matrix[row+1][column]
            position_bottom_right = matrix[row+1][column+1]

print(f"{position_top_left} {position_top_right}")
print(f"{position_bottom_left} {position_bottom_right}")
print(largest_sum)