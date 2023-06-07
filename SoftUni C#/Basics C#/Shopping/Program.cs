using System;

namespace Shopping
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            double video = double.Parse(Console.ReadLine()) * 250;
            double processor = double.Parse(Console.ReadLine()) * (video * 35 / 100);
            double RAM = double.Parse(Console.ReadLine()) * (video * 10 / 100);

            double result = processor + video + RAM;

            if ( video > processor)
            {
                result = result - (result * 15 / 100);


                if ( result <= budget)
                {
                    double finalresult = budget - result;
                    Console.WriteLine($"You have {finalresult:f2} leva left!");
                }   
                else
                {

                    double finalresult2 = result - budget;
                    Console.WriteLine($"Not enough money! You need {finalresult2:f2} leva more!");
                }    
            }

        }
    }
}
