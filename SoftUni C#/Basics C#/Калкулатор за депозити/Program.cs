using System;

namespace Калкулатор_за_депозити
{
    class Program
    {
        static void Main(string[] args)
        {
            int monthsinyear = 12;



            double value = double.Parse(Console.ReadLine());
            int period = int.Parse(Console.ReadLine());
            double increase = double.Parse(Console.ReadLine());
            double result1 = value * (increase/100);
            double result2 = result1 / monthsinyear;
            double finalresult = value + period * result2;

            Console.WriteLine(finalresult);
        }
    }
}
