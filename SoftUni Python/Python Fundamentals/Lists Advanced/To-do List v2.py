notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

print([ task for task in notes if task != 0 ])