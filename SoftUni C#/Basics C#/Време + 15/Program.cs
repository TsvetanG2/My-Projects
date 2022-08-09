using System;

namespace Време___15
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine()); // 23
            int b = int.Parse(Console.ReadLine()); //59
            int final = b + 15;
            

            if (final > 59)
            {
                a++;
                if (a > 23)
                {
                    a = 0;
                }
                final = final - 60;
                
            }
            Console.WriteLine($"{a}:{final:D2}");
        }
    }
}
