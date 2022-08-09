using System;

namespace SoftUniTask1
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = Console.ReadLine();
            string secondName = Console.ReadLine();
            int age = int.Parse(Console.ReadLine());
            string town = Console.ReadLine();
            Console.WriteLine($"Hello {firstName} {secondName}, a {age} y.o from {town}");

        }
    }
}
