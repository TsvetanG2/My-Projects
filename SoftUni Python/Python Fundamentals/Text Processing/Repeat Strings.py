text = input().split()
result = ''

for word in text:
    length = len(word)
    result += word * length

print(result)