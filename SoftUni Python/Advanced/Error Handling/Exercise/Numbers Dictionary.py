numbers_dictionary = {}
commands_list = []
line = input()

while line != "End":
    try:
        if "Search" not in commands_list:
            numbers_dictionary[line] = int(input())

        elif "Remove" not in commands_list:
            print(numbers_dictionary[line])

        else:
            del numbers_dictionary[line]
    except ValueError:
        print("The variable must be integer")
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

    while line == "Search" or line == "Remove":
        commands_list.append(line)
        line = input()

print(numbers_dictionary)