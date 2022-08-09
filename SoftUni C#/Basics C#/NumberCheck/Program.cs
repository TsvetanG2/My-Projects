using System;

namespace NumberCheck
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());

            if ( number == 0)
            {
                Console.WriteLine("No");
            }     
            else
            {
                Console.WriteLine("Yes");
            }
        }
    }
}
