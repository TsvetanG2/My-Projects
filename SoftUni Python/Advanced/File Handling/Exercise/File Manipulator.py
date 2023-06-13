from os import remove

command = input().split("-")

while command[0] != "End":
    file_name = command[1]

    if command[0] == "Create":
        file = open(f"Files/{file_name}", "w")
        file.close()

    elif command[0] == "Add":
        with open(f"Files/{file_name}", "a") as file:
            file.write(f"{command[2]}\n")

    elif command[0] == "Replace":
        to_replace = command[2]
        replace_with = command[3]

        try:
            with open(f"Files/{file_name}", "r+") as file:
                text = file.readlines()

                for row in range(len(text)):
                    text[row] = text[row].replace(to_replace, replace_with)

                file.write("".join(text))
        except FileNotFoundError:
            print("An error occurred")

    elif command[0] == "Delete":
        try:
            remove(f"Files/{file_name}")
        except FileNotFoundError:
            print("An error occurred")

    command = input().split("-")