text = input()

stack_text = list(text)

while stack_text:
    removed_element = stack_text.pop()
    print(removed_element, end='')