a = {}

for letter in input():
    a[letter] = a.get(letter, 0) + 1

for letter, times in sorted(a.items()):
    print(f"{letter}: {times} time/s")