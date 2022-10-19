import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
numbers = "123456789"
special_character = "!@#$?&"

Use_for = lower_case + upper_case + numbers + special_character
minimum_length_for_pass = 12
maximum_length_for_pass = 20
password_lenght = random.randint(minimum_length_for_pass, maximum_length_for_pass)

password = "".join(random.sample(Use_for, password_lenght))
print(f'Generated Password: {password}')