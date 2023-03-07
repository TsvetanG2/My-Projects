text = input()
result = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

#for char in text:
    #if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
       # result.append(char)

print(''.join(result))