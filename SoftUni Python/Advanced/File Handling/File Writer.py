def create_file():
    file_name = 'my_first_file.txt'
    content = "I just created my first file!"

    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(content)
    except IOError:
        print(f"An error occurred while creating the file '{file_name}'.")


create_file()