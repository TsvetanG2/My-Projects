using System;

namespace УчебниМатериали
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());
            int c = int.Parse(Console.ReadLine());
            double d = double.Parse(Console.ReadLine());
            double result1 = a * 5.80;
            double result2 = b * 7.20;
            double result3 = c * 1.20;
            double result4 = result1 + result2 + result3;
            double finalresult = result4 - (result4 * d/100);

            Console.WriteLine(finalresult);

        }
    }
}
