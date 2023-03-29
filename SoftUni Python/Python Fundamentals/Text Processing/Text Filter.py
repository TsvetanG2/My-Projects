banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        text.replace(word, "*" * len(word))
print(text)