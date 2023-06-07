number = int(input())

for _ in range(number):
    number_2 = int(input())
    if number_2 == 88:
        print("Hello")
    elif number_2 == 86:
        print("How are you?")
    elif number_2 < 88:
        print("GREAT!")
    else:
        print("Bye.")
