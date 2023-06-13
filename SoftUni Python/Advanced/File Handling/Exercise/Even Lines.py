symbols = ["-", ",", ".", "!", "?"]

with open("Files/ex1_file.txt", "r") as even_lines_file:
    text = [row.split() for row in even_lines_file.readlines()]

for sublist in range(len(text)):
    for i in range(len(text[sublist])):
        for symbol in text[sublist][i]:
            if symbol in symbols:
                text[sublist][i] = text[sublist][i].replace(symbol, "@")

[print(" ".join(text[i][::-1])) for i in range(len(text)) if i % 2 == 0]