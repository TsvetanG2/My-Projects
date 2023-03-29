def find_idx(num_list, num):
    for num_idx in range(len(num_list)):
       if num_list[num_idx] == num:
           return num_idx

    return -1


numbers = list(input().split())

while True:
    line = input()
    if line == 'Finish':
        break

    command_args = line.split()
    command = command_args[0]
    number = command_args[1]

    if command == 'Add':
        for num in numbers:
            if num not in numbers[0]:
                numbers.append(num)
    elif command == 'Remove':
        for num in numbers:
            if num in numbers[1]:
                numbers.remove(num)
    elif command == 'Replace':
        new_number = numbers[1]

        if number in numbers:
            numbers = [item.replace(new_number, number) for item in numbers]

    elif command == 'Collapse': 
        for num in numbers:
            if num < number[0]:
                numbers.remove(num)

print(' '.join(numbers))
