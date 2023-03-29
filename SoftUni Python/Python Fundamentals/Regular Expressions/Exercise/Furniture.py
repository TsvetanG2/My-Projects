import re


pattern = r'^>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)$'

total_price = 0
bought_items = []
while True:
    line = input()
    if line == 'Purchase':
        break

    matches = re.findall(pattern, line)
    if not matches:
        continue

    groups = matches[0]
    for match in matches:

        item = match[0]
        price = float(match[1])
        quantity = int(match[3])

        bought_items.append(item)
        total_price += price * quantity


print(f'Bought furniture:')
print('\n'.join(bought_items))
print(f'Total money spend: {total_price:.2f}')