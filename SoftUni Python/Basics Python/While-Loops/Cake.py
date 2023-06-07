length_cake = int(input())
width_cake = int(input())
cake_pieces = length_cake * width_cake

command = input()

while command != "STOP":
    pieces_taken = int(command)
    cake_pieces -= pieces_taken

    if cake_pieces <= 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break

    command = input()

if command == "STOP":
    print(f'{abs(cake_pieces)} pieces are left.')