using System;

namespace HotelRooms
{
    class Program
    {
        static void Main(string[] args)
        {
            string month = Console.ReadLine();
            int nights = int.Parse(Console.ReadLine());

            double price = 0;
            string room = "Studio";
            string room2 = "Apartment";
            bool all = room == "Studio" || room2 == "Apartment";
            double total = price * nights;

            if (month == "May" || month == "Octomber")
            {

            }

        }

    }
}
