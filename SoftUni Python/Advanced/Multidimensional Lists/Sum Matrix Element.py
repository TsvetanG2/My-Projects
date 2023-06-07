rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_nums = 0

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    sum_nums += sum(inner_list)
    #numbers_as_strings = input().split(", ")
    #for num_as_str in numbers_as_strings:
        #inner_list.append(num_as_str)
    matrix.append(inner_list)

print(sum_nums)
print(matrix)
