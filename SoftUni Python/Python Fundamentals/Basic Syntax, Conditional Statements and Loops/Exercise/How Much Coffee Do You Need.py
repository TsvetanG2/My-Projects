coffee_counter = 0
while True:
    line = input()
    if line == "END":
        break

    if line == 'coding' or line == 'cat' or line == 'dog' or line == 'movie':
        coffee_counter += 1
    elif line == 'CODING' or line == 'CAT' or line == 'DOG' or line == 'MOVIE':
        coffee_counter += 2

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)