import math

canturies = int(input())

years = canturies * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{canturies} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')