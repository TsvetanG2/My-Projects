nums = [1, 20, -3, 4]

print(nums)

#Подреждане на числата от най-голямо към най-малко,включително и -3

new_ = sorted(nums, key=lambda x: -x)

#Подреждане на числата от най-голямо към най-малко,включително и -3, без да се използва lambda:

new_ = sorted(nums, reverse=True)

#Подреждане на числата от най-малко към най-голямо,включително

new_2 = sorted(nums, key=lambda x: x)
print("Подреждане на числата от най-голямо към най-малко,включително и -3")
print(new_)
print("Подреждане на числата от най-малко към най-голямо,включително")
print(new_2)