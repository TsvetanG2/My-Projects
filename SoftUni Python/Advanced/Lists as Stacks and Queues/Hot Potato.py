from collections import deque


names = deque(input().split())
toss = int(input()) - 1

while len(names) > 1:
    names.rotate(-toss)
    removed_name = names.popleft()
    print(f"Removed {removed_name}")

print(f"Last is {names.popleft()}")