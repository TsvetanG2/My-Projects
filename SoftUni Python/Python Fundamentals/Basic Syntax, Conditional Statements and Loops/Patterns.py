number = int(input())

#forwards
for i in range(1, number + 1):
    for j in range(0, i):
        print('*', end ='')
    print('')

#backwards
for i in range(number - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print('')