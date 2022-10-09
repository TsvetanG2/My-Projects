fruit = input()
day = input()
quality = float(input())
if day == 'Monday' or day == "Tuesday" or day == "Wednesday" or day =='Thursday' or day == "Friday":
    if fruit == 'banana':
        print(f"{quality * 2.50:.2f}")
    elif fruit== 'apple':
        print(f"{quality * 1.20:.2f}")
    elif fruit=='grapefruit':
        print(f"{quality * 1.45:.2f}")
    elif fruit=='kiwi':
        print(f"{quality * 2.70:.2f}")
    elif fruit=='orange':
        print(f"{quality * 0.85:.2f}")
    elif fruit=='pineapple':
        print(f"{quality * 5.50:.2f}")
    elif fruit=='grapes':
        print(f"{quality * 3.85:.2f}")
    else:
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        print(f"{quality * 2.70:.2f}")
    elif fruit == 'apple':
        print(f"{quality * 1.25:.2f}")
    elif fruit == 'grapefruit':
        print(f"{quality * 1.60:.2f}")
    elif fruit == 'kiwi':
        print(f"{quality * 3.0:.2f}")
    elif fruit == 'orange':
        print(f"{quality * 0.90:.2f}")
    elif fruit == 'pineapple':
        print(f"{quality * 5.60:.2f}")
    elif fruit == 'grapes':
        print(f"{quality * 4.20:.2f}")
    else:
        print('error')
else:
    print("error")
