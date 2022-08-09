using System;
using System.Collections.Generic;

namespace ListNames_Exercise
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> names = new List<string>();

            names.Add("Petar");
            names.Add("Yasenr");
            names.Add("Bobby");
            names.Add("Koko");
            names.Add("Des");
            names.Add("Marian");

            //foreach (var name in names)
            //{
            //     Console.WriteLine(name);
            // }

            // Друг Метод

            Console.WriteLine(string.Join(", ", names));

            names.Insert(1, "Ceco");

            names.Remove("Koko");

            Console.WriteLine(string.Join(", ", names));
            Console.WriteLine($"Count: {names.Count}");

            bool isNameInList = names.Contains("Petar");

            if (isNameInList)
            {
                Console.WriteLine("Petar is in the list");
            }
            else
            {
                Console.WriteLine("No");
            }

            names.Sort();
            names.Reverse();
            Console.WriteLine(string.Join(", ", names));

        }
    }
}
