def courses(seq):

    course_dict = {}

    while seq != "end":

        seq = seq.split(" : ")
        course = seq[0]
        user = seq[1]

        if course not in course_dict:
            course_dict[course] = list()

        course_dict[course].append(user)

        seq = input()

    for k, v in course_dict.items():
        print(f'{k}: {len(course_dict[k])}')
        result = '\n-- '.join(v)
        print(f"-- {result}")


sequence = input()
courses(sequence)