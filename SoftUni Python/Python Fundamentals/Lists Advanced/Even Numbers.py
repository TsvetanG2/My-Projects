number_list = list(map(int, input().split(', ')))

found_indecies_or_no = map(
    lambda x: x if number_list[x] % 2 == 0 else 'no',
    range(len(number_list))
)

#found_indecies_or_no = [el for el in number_list if el % 2 == 0
    #                    else 'no', range(len(number_list))]
even_indecies = list(filter(lambda a: a != 'no', found_indecies_or_no))
print(even_indecies)