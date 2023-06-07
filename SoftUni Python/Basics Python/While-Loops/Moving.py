width_of_space = int(input())
lenght_of_space = int(input())
heigth_of_space = int(input())
boxes_sum = 0
total_of_space = width_of_space * lenght_of_space * heigth_of_space

command = input()

while command != "Done":
    boxes = int(command)
    boxes_sum += boxes

    if total_of_space <= boxes_sum:
        break

    command = input()


diff = abs(boxes_sum - total_of_space)
if total_of_space <= boxes_sum:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')


