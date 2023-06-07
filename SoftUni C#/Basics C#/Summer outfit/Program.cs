using System;

namespace Summer_outfit
{
    class Program
    {
        static void Main(string[] args)
        {
            double degrees = double.Parse(Console.ReadLine());
            string timeofDay = Console.ReadLine();
            string outfit = "";
            string shoes = "";

            if (degrees > 10 && degrees <= 18)
            {
                if (timeofDay == "Morning")
                {
                    outfit = "Sweatshirt";
                    shoes = "Sneakers";
                }
                else if (timeofDay == "Afternoon")
                {
                    outfit = "T-shirt";
                    shoes = "Sandals";
                }
                else if (timeofDay == "Evening")
                {
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }
                Console.WriteLine($"It's {degrees} degrees, get your {outfit} and {shoes}.");
            }
            else if (degrees > 18 && degrees <= 24)
            {
                if (timeofDay == "Morning")
                {
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }
                else if (timeofDay == "Afternoon")
                {
                    outfit = "T-Shirt";
                    shoes = "Sandals";
                }
                else if (timeofDay == "Evening")
                {
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }
                Console.WriteLine($"It's {degrees} degrees, get your {outfit} and {shoes}.");
            }
            else if (degrees >= 25)
            {
                if (timeofDay == "Morning")
                {
                    outfit = "T-Shirt";
                    shoes = "Sandals";
                }
                else if (timeofDay == "Afternoon")
                {
                    outfit = "Swim suit";
                    shoes = "Barefoot";
                }
                else if (timeofDay == "Evening")
                {
                    outfit = "Shirt";
                    shoes = "Moccasins";
                }
                Console.WriteLine($"It's {degrees} degrees, get your {outfit} and {shoes}.");
            }
            else
            {

            }
            
        }
    }
}
