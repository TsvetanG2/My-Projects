def perfect_or_not(number):
    sum = 0
    for n in range(1, number):
        if number % n == 0:
            sum += n
    if sum == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())

perfect_or_not(num)