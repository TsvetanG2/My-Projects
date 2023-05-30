data = tuple(map(float, input().split()))

occ = {}

for el in data:
    occ[el] = data.count(el)

for num, count in occ.items():
    print(f"{num} - {count} times")

