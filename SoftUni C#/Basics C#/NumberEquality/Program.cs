using System;

namespace NumberEquality
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int maxnumber = 0;
            int mixnumber = 0;
            
            for (int i = 0; i < n; i++)
            {
                int a = int.Parse(Console.ReadLine());
                if (a >= maxnumber)
                {
                    maxnumber = a;
                }
                if (a < mixnumber)
                {
                    mixnumber = a;
                }
            }Console.WriteLine($"Max number: {maxnumber}");
            Console.WriteLine($"Min number: {mixnumber}");
        }
    }
}
