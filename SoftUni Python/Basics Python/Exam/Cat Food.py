cats_sum = int(input())

food_sum = 0
cat_group_one = 0
cat_group_two = 0
cat_group_three = 0

for i in range(1, cats_sum + 1):
    eaten_food_per_cat = int(input())
    food_sum += eaten_food_per_cat

    if eaten_food_per_cat >= 100 and eaten_food_per_cat < 200:
        cat_group_one += 1
    elif eaten_food_per_cat >= 200 and eaten_food_per_cat < 300:
        cat_group_two += 1
    elif eaten_food_per_cat >= 300 and eaten_food_per_cat < 400:
        cat_group_three += 1

print(f'Group 1: {cat_group_one} cats.')
print(f'Group 2: {cat_group_two} cats.')
print(f'Group 3: {cat_group_three} cats.')

food_in_grams = food_sum
food_in_kg = food_sum / 1000
food_price = food_in_kg * 12.45

print(f'Price for food per day: {food_price:.2f} lv.')