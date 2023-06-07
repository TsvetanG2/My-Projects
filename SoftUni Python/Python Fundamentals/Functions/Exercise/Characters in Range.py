def CharacterInRange(start, end):
    result = []
    for i in range(ord(start) + 1, ord(end)):
        result.append(chr(i))

    return result


char1 = input()
char2 = input()

result_chars = CharacterInRange(char1, char2)
print(' '.join(result_chars))

