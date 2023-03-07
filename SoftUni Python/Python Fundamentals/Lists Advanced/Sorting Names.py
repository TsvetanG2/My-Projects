names = input().split(', ')

#Сортира имената по брой на буквите на обрато, тоест от най-дългото към най-късото. При (-len(x), x)
# ги сортира по азбучен ред

print(sorted(names, key=lambda x: (-len(x), x)))

#Друг вариант:
#sorted_names = sorted(names, key=lambda x: (-len(x), x)))
#print(sorted_names)