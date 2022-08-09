using System;

namespace NumSequels
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int left = 0;
            int right = 0;

            for (int i = 0; i < n; i++)
            {
                int currentNumber = int.Parse(Console.ReadLine());
                left += currentNumber;
            }
            for (int i = 0; i < n; i ++)
            {
                int currentnumber = int.Parse(Console.ReadLine());
                right += currentnumber;
            }
            if (left == right)
            {
                Console.WriteLine($"Yes, sum = {left}");
            }
            else
            {
                Console.WriteLine($"No, diff = {Math.Abs(left - right)}");
            } 
                
        }
    }
}
