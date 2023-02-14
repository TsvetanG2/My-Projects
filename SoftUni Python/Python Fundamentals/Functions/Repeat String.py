string = input()
n = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, n)
print(result)