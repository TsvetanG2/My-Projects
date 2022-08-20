﻿using System;

namespace GoldMine
{
    class Program
    {
        static void Main(string[] args)
        {
            int locations = int.Parse(Console.ReadLine());

            double goldfortheday = 0;

            for (int i = 0; i <= locations; i++)
            {
                double expectedgold = double.Parse(Console.ReadLine());
                int days = int.Parse(Console.ReadLine());

                while (goldfortheday != 0)
                {
                    double diggedgold = double.Parse(Console.ReadLine());

                    if (diggedgold >= 0)
                    {
                        diggedgold += goldfortheday;
                    }

                }

                goldfortheday /= days;

                if (goldfortheday >= expectedgold)
                {
                    Console.WriteLine($"Good job! Average gold per day: {goldfortheday:f2}.");
                }
                else
                {
                    goldfortheday -= expectedgold;

                    Console.WriteLine($"You need: {Math.Abs(goldfortheday):f2}.");
                }
                    
                        
            }
        }
    }
}
