import random, pyautogui, string

digits = list(string.digits)
iteration_counter = 0
password = input('Enter password:')

guess_password = ''

while guess_password != password:
    guess_password = random.choices(digits, k=len(password))
    iteration_counter += 1
    print(f'>>>>{"".join(guess_password)}<<<<')


    if guess_password == List(password):
        print(f'Your password is: {"".join(guess_password)}'    
              f'\nNumber of iteration is: {iteration_counter}')
        break