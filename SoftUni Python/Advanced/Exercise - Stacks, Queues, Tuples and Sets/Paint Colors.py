from collections import deque

words = deque(input().split())  # d yel blu e low redd

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(result): # iterate over every secondary color that we have
    if not req_colors[color].issubset(result):  # check if we have the needed colors to have the secondary color
        result.remove(color)

print(result)