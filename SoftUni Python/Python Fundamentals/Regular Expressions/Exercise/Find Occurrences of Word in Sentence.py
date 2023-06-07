import re

text = input().lower()
target = input().lower()

matched = re.findall(rf'\b{target}\b', text)

print(len(matched))