import random

while True:
    Mo = input("Izberi si opciq: [Ceco zobi, Mo e slab, Mo zavijda]: ")
    choose = ["Ceco zobi", "Mo e slab", "Mo zavijda"]
    Ceco = random.choice(choose)

    print(f"Otgovor Mo: {Mo}")
    print()
    print(f"Otgovor Ceco: {Ceco}")
    print()

    if Mo == Ceco:
        print("Mo zavijda")


    if Mo == "Ceco zobi":
        if Ceco == "Mo e slab":
            print("Mo zavijda i e sparujen Plik")

        else:
            print("30 kila nad men, 30 kila sila pod men")

    if Mo == "Mo e slab":
        if Ceco == " Mo zavijda":
            print("Bebe mo ne e slab,"
                  " toi samo zavijda")

        else:
            print("Da taka e")

    if Mo == "Mo zavijda":
        if Ceco == "Ceco zobi":
            print("Ceco nikoga ne e zobil, toi e naturalen")

        else:
            print("Ceco e naturalen, mo zobi")

    continue
    print()