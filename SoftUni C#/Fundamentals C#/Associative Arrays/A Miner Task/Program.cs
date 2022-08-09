using System;
using System.Collections.Generic;

namespace A_Miner_Task
{
    class Program
    {
        static void Main(string[] args)
        {
            var items = new Dictionary<string, int>();
            string resources = Console.ReadLine();

            while (resources != "stop")
            {
                int quantity = int.Parse(Console.ReadLine());
                if (!items.ContainsKey(resources))
                {
                    items.Add(resources, 0);
                }
                items[resources] += quantity;
                resources = Console.ReadLine();
            }

            foreach (var item in items)
            {
                Console.WriteLine($"{item.Key} -> {item.Value}");
            }
        }
    }
}
