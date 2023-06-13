from collections import Counter


def count_word_occurrences():
    words_file = 'words.txt'
    text_file = 'text.txt'
    output_file = 'results.txt'

    # Read the list of words from words.txt
    with open(words_file, 'r') as file:
        words = [word.strip().lower() for word in file.readlines()]

    # Count the occurrences of words in text.txt
    with open(text_file, 'r') as file:
        text = file.read().lower()

    word_counts = Counter(text.split())

    # Sort words by frequency in descending order
    sorted_words = sorted(words, key=lambda word: word_counts[word], reverse=True)

    # Write the results into results.txt
    with open(output_file, 'w') as file:
        for word in sorted_words:
            count = word_counts[word]
            file.write(f"{word}: {count}\n")

    print(f"Results written to {output_file}.")


count_word_occurrences()
