import os


def delete_file():
    file_name = 'my_first_file.txt'

    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print("File already deleted!")


delete_file()