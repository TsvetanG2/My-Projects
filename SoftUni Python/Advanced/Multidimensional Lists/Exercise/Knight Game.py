size = int(input())

matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1), # up 2 left 1
    (-2, 1), # up 2 right 1
    (-1, -2), # up 1 left 2
    (-1, 2), # up 1 left 2
    (2, -1), # down 2 left 1
    (2, 1), # down 2 right 1
    (1, 2), # down 1 right 2
    (1, -2), # down 1 left 2
)

removed_knights = 0

while True:
    max_attacks = 0
    knights_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knights_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knights_with_most_attacks_pos:
        matrix[knights_with_most_attacks_pos[0]][knights_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
