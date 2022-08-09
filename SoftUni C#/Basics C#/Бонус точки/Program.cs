using System;

namespace Бонус_точки
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            double bonus = 0.0;

            if ( a <= 100)
            {
                bonus = 5;
            }
            else if ( a > 1000)
            {
                bonus = a * 0.1;
            }
            else
            {
                bonus = a * 0.2;
            }
            if ( a % 2 == 0)
            {
                bonus = bonus + 1;
            }
            else if ( a % 10 == 5)
            {
                bonus += 2;
            }
            Console.WriteLine(bonus);
            Console.WriteLine(bonus + a);
        }
    }
}
