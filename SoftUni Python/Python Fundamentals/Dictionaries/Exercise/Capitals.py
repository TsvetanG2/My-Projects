countries = input().split(", ")
capitals = input().split(", ")

#Вариант 1
capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}

#Вариант 1 с резултат
result = [f'{country} -> {capital}' for country, capital in capital_by_country.items()]

#Вариант 2
#capital_by_country = {}
#for idx in range(len(countries)):
  #  country = countries[idx]
   # capital = capitals[idx]
   # capital_by_country[country] = capital

print('\n'.join(result))