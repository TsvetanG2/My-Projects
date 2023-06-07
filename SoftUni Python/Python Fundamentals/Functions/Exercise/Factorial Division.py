def factorial(num1, num2):
    fact1 = 1
    fact2 = 1
    for i in range(1, num1 + 1):
        fact1 *= i
    for k in range(1, num2 + 1):
        fact2 *= k

    result = fact1 / fact2
    print(f"{result:.2f}")


number1 = int(input())
number2 = int(input())

factorial(number1, number2)