first = input()
second = input()

result = first
for idx in range(len(first)):

    if first[idx] == second[idx]:
        continue

    result = second[:idx + 1] + first[idx + 1:]
    print(result)