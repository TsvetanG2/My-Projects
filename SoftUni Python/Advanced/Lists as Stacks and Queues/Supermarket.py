from collections import deque


customers = deque()

while True:
    name = input()
    if name == "Paid":
        while customers:
            print(customers.popleft())
        continue
    elif name == "End":
        break

    customers.append(name)
print(f"{len(customers)} people remaining.")
#while name != "Paid":
  #  customers.append(name)
  #  name = input()



