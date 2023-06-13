def repeat_text():
    text = input()
    times = input()

    try:
        times = int(times)
        for _ in range(times):
            print(text, end='')
    except ValueError:
        print("Variable times must be an integer.")


repeat_text()