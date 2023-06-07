using System;

namespace Invalidnumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            if (number >= 100 && number <= 200)
            {
                Console.WriteLine();
            }
            else if (number == 0)
            {
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine("invalid");
            }
        }
    }
}
