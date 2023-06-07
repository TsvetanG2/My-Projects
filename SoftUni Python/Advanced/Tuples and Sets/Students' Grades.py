from statistics import mean
from collections import defaultdict


n_line = int(input())

student_grades = defaultdict(lambda: [])

for i in range(n_line):
    name, grade = input().split()
    grade = float(grade)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg = mean(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")
