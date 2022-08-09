using System;

namespace OddSeq
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            int oddsum = 0;
            int evensum = 0;

            for (int i = 1; i <= n; i++)
            {
                int number = int.Parse(Console.ReadLine());
                if (i % 2 == 0)
                {
                    evensum += number;
                    Console.WriteLine("Yes");
                    Console.WriteLine($"Sum = {evensum}");
                }
                else
                {
                    oddsum += number;
                    Console.WriteLine("No");
                    Console.WriteLine($"Diff = {Math.Abs(oddsum - evensum)}");
                }

            }
            
        }  
    }
}
