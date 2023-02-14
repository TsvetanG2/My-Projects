def progress_bar(num):
    percents = ""
    if num == "100":
        percents += "%%%%%%%%%%"
        print(f"100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        for i in num:
            percents += "%" * int(num[0])
            break
    if len(percents) < 10:
        percents += "." * (10 - len(percents))
        print(f"{num}% [{percents}]")
        print("Still loading...")


number = input()

progress_bar(number)