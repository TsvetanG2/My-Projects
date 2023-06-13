output_file = open("Files/ex2_output.txt", "a")

with open("Files/ex1_file.txt", "r") as text_file:
    text = text_file.readlines()

for i in range(len(text)):
    row = text[i]
    letters = 0
    marks = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif not symbol.isalpha() and not symbol.isspace():
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(row[:-1])} ({letters})({marks})\n")

output_file.close()