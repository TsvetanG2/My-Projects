using System;

namespace ReverseCount
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = int.Parse(Console.ReadLine());

            for (int n = i ; i >= 1 ; i--)
            {
                Console.WriteLine(i);
            }
        }
    }
}
