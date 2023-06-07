using System;

namespace CinemaTickets
{
    class Program
    {
        static void Main(string[] args)
        {
            string day = Console.ReadLine();
            int price = 0;

            switch (day)
            {
                case "Monday":
                case "Tuesday":
                case "Friday":
                    price = 12;
                    Console.WriteLine(price);
                    break;
                case "Wednesday":
                case "Thrusday":
                    price = 14;
                    Console.WriteLine(price);
                    break;
                case "Saturday":
                case "Sunday":
                    price = 16;
                    Console.WriteLine(price);
                    break;
                default:
                    break;   
            }
        }
    }
}
