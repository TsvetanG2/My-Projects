initial_stringy = input().split(", ")


def palindrome(initial_string):
    is_palindrome = False
    for i in range(len(initial_stringy)):
        is_palindrome = False
        current_i = initial_stringy[i]
        word = ""
        word2 = ""
        for ch in range(len(current_i)):
            word += current_i[ch]
        lenght_i = len(current_i)
        for character in range(lenght_i - 1, -1, -1):
            word2 += current_i[character]
        if word == word2:
            is_palindrome = True
        print(is_palindrome)


palindrome(initial_stringy)