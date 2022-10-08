our_of_exam = int(input())
minute_of_exam = int(input())
our_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time = (our_of_exam * 60) + minute_of_exam
arrival_time = (our_of_arrival * 60) + minute_of_arrival
difference = abs(exam_time - arrival_time)
hour = difference // 60
minutes = difference % 60

if exam_time == arrival_time:
    print("On time")
elif exam_time > arrival_time:
    if difference <= 30:
        print("On time")
        print(f"{minutes} minutes before the start")
    elif 30 < difference < 60:
        print("Early")
        print(f"{minutes} minutes before the start")
    elif difference > 59:
        print("Early")
        print(f"{hour}:{minutes:02d} hours before the start")
elif arrival_time > exam_time:
    print("Late")
    if difference < 60:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hour}:{minutes:02d} hours after the start")