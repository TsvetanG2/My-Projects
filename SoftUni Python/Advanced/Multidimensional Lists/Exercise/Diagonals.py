n = int(input())

martixx = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary = [martixx[r][r] for r in range(n)]
secondary = [martixx[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
