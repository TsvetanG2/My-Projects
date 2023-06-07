using System;

namespace VacationBookList
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());
            int c = int.Parse(Console.ReadLine());
            int result = a / b;
            int result2 = result / c;

            Console.WriteLine(result2);

        }
    }
}
