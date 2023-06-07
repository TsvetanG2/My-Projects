from collections import deque

numbers = deque(input().split())

numbers.reverse()
final_numbers = " ".join(numbers)

print(final_numbers)
