using System;
using System.Collections.Generic;

namespace Orders
{
    class Program
    {
        static void Main(string[] args)
        {
            // създаваме 2 dictorities
            // Първият (1) ще има NameOfTheProduct (Име на продукта): value priceOfTheProduct
            // Вторият (2) ще има NameOfTheProduct (Име на продукта): value quantityOfTheProduct

            var orders = new Dictionary<string, double>();
            var newOrders = new Dictionary<string, int>();

            var input = Console.ReadLine();

            while (input != "buy")
            {
                var cmd = input.Split();
                var productname = cmd[0];
                double productPrice = double.Parse(cmd[1]);
                int quantity = int.Parse(cmd[2]);

                if (!orders.ContainsKey(productname))
                {
                    orders.Add(productname, productPrice);
                    newOrders.Add(productname, quantity);

                }
                else if (orders.ContainsKey(productname))
                {
                    orders.Remove(productname);
                    orders.Add(productname, productPrice);
                    newOrders[productname] += quantity;
                }
                input = Console.ReadLine();
            }

            foreach (var order in orders)
            {
                foreach(var newOrder in newOrders)
                {
                    if (order.Key == newOrder.Key)
                    {
                        Console.WriteLine($"{order.Key} -> {order.Value * newOrder.Value:f2}");
                    }
                }
            }
        }
    }
}
