count_group = int(input())

musala_sum = 0
monblan_sum = 0
kilimandjaro_sum = 0
k2_sum = 0
everest_sum = 0

total_sum = 0

for i in range(1, count_group + 1):
    people = int(input())
    total_sum += people

    if people <= 5:
        musala_sum += people
    elif people <= 12:
        monblan_sum += people
    elif people <= 25:
        kilimandjaro_sum += people
    elif people <= 40:
        k2_sum += people
    elif people >= 41:
        everest_sum += people


musala_percent = musala_sum / total_sum * 100
print(f'{musala_percent:.2f}%')

monblan_percent = monblan_sum / total_sum * 100
print(f'{monblan_percent:.2f}%')

kilimandjaro_percent = kilimandjaro_sum / total_sum * 100
print(f'{kilimandjaro_percent:.2f}%')

k2_percent = k2_sum / total_sum * 100
print(f'{k2_percent:.2f}%')

everest_percent = everest_sum / total_sum * 100
print(f'{everest_percent:.2f}%')