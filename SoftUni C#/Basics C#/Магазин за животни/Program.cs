using System;

namespace Магазин_за_животни
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = double.Parse(Console.ReadLine());
            double b = 2.50;
            double result = a * b;
            double c = double.Parse(Console.ReadLine());
            double e = 4;
            double result2 = c * e;
            double finalresult = result + result2;

            Console.WriteLine($"{finalresult} lv.");

        }
    }
}
