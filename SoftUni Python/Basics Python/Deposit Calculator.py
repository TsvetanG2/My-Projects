deposit = float(input())
time = int(input())
interest = float(input()) * 0.01

result = deposit + time * ((deposit * interest) / 12)
print(result)