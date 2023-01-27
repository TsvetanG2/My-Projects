n = int(input())

start = 97

for i in range(start, start + n):
    for j in range(start, start + n):
        for h in range(start, start + n):
            print(chr(i), chr(j), chr(h), sep='')