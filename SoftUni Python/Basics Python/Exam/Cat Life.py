cats_birth = input()
cats_gender = input()

cats_life = 0

Is_cat_valid = True

if cats_birth == 'British Shorthair':
    if cats_gender == 'm':
        cats_life = 13
    if cats_gender == 'f':
        cats_life = 14
elif cats_birth == 'Siamese':
    if cats_gender == 'm':
        cats_life = 15
    if cats_gender == 'f':
        cats_life = 16
elif cats_birth == 'Persian':
    if cats_gender == 'm':
        cats_life = 14
    if cats_gender == 'f':
        cats_life = 15
elif cats_birth == 'Ragdoll':
    if cats_gender == 'm':
        cats_life = 16
    if cats_gender == 'f':
        cats_life = 17
elif cats_birth == 'American Shorthair':
    if cats_gender == 'm':
        cats_life = 12
    if cats_gender == 'f':
        cats_life = 13
elif cats_birth == 'Siberian':
    if cats_gender == 'm':
        cats_life = 11
    if cats_gender == 'f':
        cats_life = 12
else:
    Is_cat_valid = False
    print(f'{cats_birth} is invalid cat!')


cats_life_in_months = (cats_life * 12) / 6
if Is_cat_valid:
    print(f'{int(cats_life_in_months)} cat months')
