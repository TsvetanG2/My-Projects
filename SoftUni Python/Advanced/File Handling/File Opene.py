file = open("text.txt")
content = file.read()
print(content)

Found_file = False

if Found_file:
    print("File not found")
else:
    print("File found")
