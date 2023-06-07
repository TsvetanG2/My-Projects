from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

for order in orders.copy(): #прави копие на данните и ги прехвърля в копиран списък
    if food >= order:
        orders.popleft()
        food -= order

    else:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break

else:
    print(f'Orders complete')

#Ползваме for/else структура - Тоест ако не изпълним условието във if и цикъла не бъде break-нат, то тогава влизаме
# в else




