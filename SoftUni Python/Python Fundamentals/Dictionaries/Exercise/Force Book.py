def check_for_line(dictionary1, side1, name1):
    current_list = [x for x in dictionary.values() if name1 in x]
    if side1 not in dictionary1.keys() and len(current_list) == 0:
        dictionary1[side1] = [name1]
    elif side1 in dictionary1.keys() and len(current_list) == 0:
        dictionary1[side1].append(name1)


def check_for_arrow(dictionary2, name2, side2):
    current_list2 = [z for z in dictionary.values() if name2 in z]
    if side2 not in dictionary2.keys() and len(current_list2) == 0:
        dictionary2[side2] = [name2]
    elif side2 in dictionary2.keys() and len(current_list2) == 0:
        dictionary2[side2].append(name2)
    else:
        for item in dictionary2.keys():
            if name2 in dictionary2[item]:
                dictionary2[item].remove(name2)
                break
        if side2 not in dictionary2.keys():
            dictionary2[side2] = [name2]
        else:
            dictionary2[side2].append(name2)
    print(f"{name2} joins the {side2} side!")


line = input()
dictionary = {}
while line != "Lumpawaroo":
    if "|" in line:
        command = line.split(" | ")
        side = command[0]
        name = command[1]
        check_for_line(dictionary, side, name)
    else:
        command = line.split(" -> ")
        name = command[0]
        side = command[1]
        check_for_arrow(dictionary, name, side)
    line = input()

keys_to_pop = []

for key, value in dictionary.items():
    if len(dictionary[key]) == 0:
        keys_to_pop.append(key)
    else:
        print(f"Side: {key}, Members: {len(dictionary[key])}")
        for v in value:
            print(f"! {v}")

for k in keys_to_pop:
    dictionary.pop(k)