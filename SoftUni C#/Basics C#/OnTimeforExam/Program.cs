using System;

namespace P08.OnTimeForTheExam
{
    class OnTimeForTheExam
    {
        static void Main(string[] args)
        {
            const int MINUTES_IN_A_HOUR = 60;
            const int EARLY_IN_MINUTES = 30;

            int examHour = int.Parse(Console.ReadLine()); // 570
            int examMinute = int.Parse(Console.ReadLine());
            int arrivalHour = int.Parse(Console.ReadLine()); // 580
            int arrivalMinute = int.Parse(Console.ReadLine());

            int examHourInMinutes = examHour * MINUTES_IN_A_HOUR;
            int examInMinutes = examHourInMinutes + examMinute;

            int arrivalHourInMinutes = arrivalHour * MINUTES_IN_A_HOUR;
            int arrivalInMinutes = arrivalHourInMinutes + arrivalMinute;

            int diff = Math.Abs(arrivalInMinutes - examInMinutes);
            int hour = diff / MINUTES_IN_A_HOUR;
            int minutes = diff % MINUTES_IN_A_HOUR;

            if (arrivalInMinutes > examInMinutes)
            {
                Console.WriteLine("Late");

                if (diff < MINUTES_IN_A_HOUR)
                {
                    Console.WriteLine($"{diff} minutes after the start");
                }
                else
                {
                    Console.WriteLine($"{hour}:{minutes:d2} hours after the start");
                }
            }
            else if (arrivalInMinutes < examInMinutes && arrivalInMinutes >= examInMinutes - EARLY_IN_MINUTES)
            {
                Console.WriteLine("On time");
                Console.WriteLine($"{diff} minutes before the start");
            }
            else if (arrivalInMinutes == examInMinutes)
            {
                Console.WriteLine("On time");
            }
            else if (arrivalInMinutes < examInMinutes - EARLY_IN_MINUTES)
            {
                Console.WriteLine("Early");

                if (diff < MINUTES_IN_A_HOUR)
                {
                    Console.WriteLine($"{diff} minutes before the start");
                }
                else
                {
                    Console.WriteLine($"{hour}:{minutes:d2} hours before the start");
                }
            }
        }
    }
}