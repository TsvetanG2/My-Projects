using System;

namespace ForCycle
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            for (n = 1; n <= 100; n += 1)
            {
                Console.WriteLine(n);
            }
        }
    }
}
