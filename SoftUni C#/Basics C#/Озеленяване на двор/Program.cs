using System;

namespace Озеленяване_на_двор
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = double.Parse(Console.ReadLine());
            double b = 7.61;
            double result = a * b;
            double result2 = result * 0.18;
            double result3 = result - result2;

            Console.WriteLine($"The fInal price is: {result3} lv.");
            Console.WriteLine($"The discount is: {result2} lv.");
        }
    }
}
