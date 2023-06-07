name = input()
grades_total = 0
failed_years = 0
years_counter = 0

while True:

    annual_grade = float(input())
    years_counter += 1

    if annual_grade < 4:
        failed_years += 1

        if failed_years > 1 or failed_years == 2:
            print(f'{name} has been excluded at {years_counter} grade')
            break

        years_counter -= 1

    else:
        grades_total += annual_grade

    if years_counter == 12:
        average_grade = grades_total / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break