def sorted1(a):
    result = sorted(a)
    return result


number = [int(x) for x in input().split()]
print(sorted1(number))