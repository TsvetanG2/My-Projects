a = input().split()
odd_occurrences_dict = {}

for word in a:
    word_lower = word.lower()

    if word_lower not in odd_occurrences_dict:
        odd_occurrences_dict[word_lower] = 0

    odd_occurrences_dict[word_lower] += 1

for (key, value) in odd_occurrences_dict.items():
    if value % 2 != 0:
        print(key, end=" ")