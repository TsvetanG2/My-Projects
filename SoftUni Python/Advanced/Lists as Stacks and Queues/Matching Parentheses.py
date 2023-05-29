stack_parant = []

text = input()

for index in range(len(text)):
    if text[index] == "(":
        stack_parant.append(index)
    elif text[index] == ")":
        start_position = stack_parant.pop()
        end_position = index + 1
        print(text[start_position:end_position])