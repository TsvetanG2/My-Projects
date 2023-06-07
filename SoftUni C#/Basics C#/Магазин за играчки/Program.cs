using System;

namespace Магазин_за_играчки
{
    class Program
    {
        static void Main(string[] args)
        {
            int discount = 50;

            double a = double.Parse(Console.ReadLine());
            double b = double.Parse(Console.ReadLine());
            double c = double.Parse(Console.ReadLine());
            double d = double.Parse(Console.ReadLine());
            double e = double.Parse(Console.ReadLine());
            double f = double.Parse(Console.ReadLine());

            double result1 = b * 2.60 + c * 3 + d * 4.10 + e * 8.20 + f * 2;
            double result2 = b + c + d + e + f;

            if (result2 > discount)
            {
                double result3 = result1 * 25/100;
                double result5 = result1 - result3;
                double rent = result5 * 10 / 100;
                double result4 = result5 - rent;


                if (result4 > a)
                {
                    result4 = result4 - a;

                    Console.WriteLine($"Yes! {result4:f2} lv left.");
                }
            }
            else if (result2 < discount)
            {
                double rent = result1 * 10 / 100;
                double final = result1 - rent;

                if (final < a)
                {
                    double final2 = a - final;

                    Console.WriteLine($"Not enough money! {final2:f2} lv needed.");
                }
            }
        }
    }
}
