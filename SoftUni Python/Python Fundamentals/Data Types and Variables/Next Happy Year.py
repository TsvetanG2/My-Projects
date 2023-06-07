year = int(input())
year_as_string = str(year)
year += 1


while len(year_as_string) != len(set(year_as_string)):
    year += 1
    year_as_string = str(year)

print(year)