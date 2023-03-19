def academy(num_ppl):
    grades = {}
    for i in range(num_ppl):
        name = input()
        grade = float(input())

        if name not in grades:
            grades[name] = list()

        grades[name].append(grade)

    for k, v in list(grades.items()):
        average_grade = sum(v) / len(v)
        if average_grade < 4.5:
            del grades[k]
        else:
            print(f"{k} -> {average_grade:.2f}")


number_of_people = int(input())
academy(number_of_people)