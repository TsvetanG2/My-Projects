food_bought = int(input())
food_in_grams = food_bought * 1000
command = input()
food_sum = 0

Is_food_finished = False

while command != "Adopted":
    grams_eaten = int(command)
    food_sum += grams_eaten

    if food_in_grams < food_sum:
        Is_food_finished = True

    command = input()

diff = abs(food_in_grams - food_sum)

if Is_food_finished:
    print(f'Food is not enough. You need {diff} grams more.')
else:
    print(f'Food is enough! Leftovers: {diff} grams.')