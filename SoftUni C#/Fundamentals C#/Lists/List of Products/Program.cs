using System;
using System.Collections.Generic;

namespace List_of_Products
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> products = new List<string>();
            int count = int.Parse(Console.ReadLine());

            for (int i = 0; i < count; i++)
            {
                products.Add(Console.ReadLine());
            }
            products.Sort();

            int counter = 1;

            foreach (string product in products)
            {
                Console.WriteLine($"{counter}.{product}");

                counter++;
            }
        }
    }
}
