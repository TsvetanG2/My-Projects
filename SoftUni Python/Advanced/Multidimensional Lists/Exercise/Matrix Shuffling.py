def check_valid_indicies(indices: list):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valids_cols)
    #Проверяваме дали тези неща се намират във Valid Rows и Valid Cols
    #Връща True или False


def swap_command(command: str, indices: list):
    if check_valid_indicies(indices) and command == "swap" and len(indices) == 4:
        row1, col1, row2, col2 = indices

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        #Матриците си сменят местата

        print(*[' '.join(r) for r in matrix], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valids_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]
    #Ако х е число искаме да върнеш integer - число, ако не е число го върни като string

    if command_type == "END":
        break

    swap_command(command_type, info)
