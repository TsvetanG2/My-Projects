n = int(input())

elements = set()

for i in range(n):
    for el in input().split():
        elements.add(el)

print(*elements, sep="\n")
