a = int(input())

p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0

for i in range(1, a + 1):
    currnum = int(input())
    if currnum < 200:
        p_1 += 1
    elif currnum <= 399:
        p_2 += 1
    elif currnum <= 599:
        p_3 += 1
    elif currnum <= 799:
        p_4 += 1
    elif currnum >= 800:
        p_5 += 1


percent_p1 = p_1 / a * 100
percent_p2 = p_2 / a * 100
percent_p3 = p_3 / a * 100
percent_p4 = p_4 / a * 100
percent_p5 = p_5 / a * 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')
