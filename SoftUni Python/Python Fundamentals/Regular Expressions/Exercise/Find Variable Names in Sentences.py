import re

text = input() + " "
matches = re.findall(r'\s_([A-Za-z\d]+)\s', text)

print(','.join(matches))