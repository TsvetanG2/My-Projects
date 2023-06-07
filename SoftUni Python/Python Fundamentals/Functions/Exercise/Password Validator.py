def is_valid_length(a):
    return 6 <= len(a) <= 10


def contains_alpha_numeric_chards(a):
    return password.isalnum()


def contains_at_least_2_digits(a):
    digits_counter = 0

    for ch in a:
        if ch.isdigit():
            digits_counter += 1

    return digits_counter >= 2


password = input()

is_valid = True

if not is_valid_length(password):
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not contains_alpha_numeric_chards(password):
    is_valid = False
    print("Password must consist only of letters and digits")

if not contains_at_least_2_digits(password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")