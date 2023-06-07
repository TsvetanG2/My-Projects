N1 = int(input())
N2 = int(input())
operator = input()
result = 0
even_odd = ""

if N2 == 0:
    print(f"Cannot divide {N1} by zero")
elif operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_odd}")
elif operator == "/":
    result = N1 / N2
    print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    result = N1 % N2
    print(f"{N1} % {N2} = {result}")
