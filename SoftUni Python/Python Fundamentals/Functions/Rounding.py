initial_str = input().split(" ")

def rounder():
    new_list = []
    for i in initial_str:
        current_i = round(float(i))
        new_list.append(current_i)
    return new_list

print(rounder())