using System;

namespace Баскетболну_оборудване
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());

            double result = a - (a * 40 / 100);
            double result2 = result -  (result * 20 / 100);
            double result3 = result2 * 1 / 4;
            double result4 = result3 * 1 / 5;
            double finalresult = a + result + result2 + result3 + result4;

            Console.WriteLine(finalresult);


        }
    }
}
