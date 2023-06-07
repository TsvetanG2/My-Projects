letters = input().split(", ")
dictionary = {}

for i in letters:
    ord_letter = ord(i)
    dictionary[i] = int(ord_letter)

print(dictionary)