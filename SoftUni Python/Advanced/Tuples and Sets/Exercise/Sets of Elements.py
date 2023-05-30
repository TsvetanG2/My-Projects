n, m = map(int, input().split())

first_set = {int(input()) for _ in range(n)}
second_set = {int(input()) for _ in range(m)}

print(*first_set.intersection(second_set), sep="\n")
