using System;
using System.Numerics;

namespace BigFactorialOPEN
{
    class Program
    {
        static void Main(string[] args)
        {
            int number = int.Parse(Console.ReadLine());
            BigInteger result = 1;

            for (int i = 2; i <= number; i ++)
            {
                result *= i;
            }
            Console.WriteLine(result);
        }
    }
}
