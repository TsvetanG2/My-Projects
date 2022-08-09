using System;

namespace Radiant_to_Degrees
{
    class Program
    {
        static void Main(string[] args)
        {
            double radiant = double.Parse(Console.ReadLine());
            double degrees = radiant * 180 / Math.PI;

            Console.WriteLine(degrees);
        }
    }
}
