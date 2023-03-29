import re

text = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), end=" ")