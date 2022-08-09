using System;

namespace Fishing_boat
{
    class Program
    {
        static void Main(string[] args)
        {
            double budgetgroup = double.Parse(Console.ReadLine());
            string season = Console.ReadLine();
            int fisherman = int.Parse(Console.ReadLine());
            double rent = 0.0;
            double odd = fisherman % 2;
            
            switch (season)
            {
                case "Autumn":
                    rent = 3000;
                    if (fisherman <= 6)
                    {
                        rent = rent - (rent * 0.10);
                    }
                    else if (fisherman > 6 && fisherman == 11)
                    {
                        rent = rent - (rent * 0.15);
                    }
                    else if (fisherman > 11)
                    {
                        rent = rent - (rent * 0.25);
                    }
                    break;
                case "Summer":
                    rent = 4200;
                    if (fisherman <= 6)
                    {
                        rent = rent - (rent * 0.10);
                    }
                    else if (fisherman > 6 && fisherman == 11)
                    {
                        rent = rent - (rent * 0.15);
                    }
                    else if (fisherman > 11)
                    {
                        rent = rent - (rent * 0.25);
                    }
                    else if (fisherman == odd)
                    {
                        rent *= 0.5;
                    }
                    break;
                case "Winter":
                    rent = 2600;
                    if (fisherman <= 6)
                    {
                        rent = rent - (rent * 0.10);
                    }
                    else if (fisherman > 6 && fisherman == 11)
                    {
                        rent = rent - (rent * 0.15);
                    }
                    else if (fisherman > 11)
                    {
                        rent = rent - (rent * 0.25);
                    }
                    else if (fisherman  == odd)
                    {
                        rent *= 0.5;
                    }
                    break;
            }
            if (rent > budgetgroup)
            {
                double result = rent - budgetgroup;
                Console.WriteLine($"Not enough money! You need {result:F2} leva.");
            }
            else
            {
                double result2 = budgetgroup - rent;
                Console.WriteLine($"Yes! You have {result2:F2} leva left.");
            }
        }
    }
}
