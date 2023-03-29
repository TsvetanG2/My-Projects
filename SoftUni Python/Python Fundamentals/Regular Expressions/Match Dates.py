import re

text = input()

pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
results = re.finditer(pattern, text)

for result in results:
    result_data = result.groupdict()
    print(f"Day: {result_data['Day']}, Month: {result_data['Month']}, Year: {result_data['Year']}")