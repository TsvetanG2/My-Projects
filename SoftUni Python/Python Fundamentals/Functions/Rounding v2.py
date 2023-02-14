string = input().split(" ")

def rounding():
    round_list = []
    for i in string:
        current_i = round(float(i))
        round_list.append(current_i)
    return round_list

print(rounding())