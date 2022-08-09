using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Box
    {
        public string SerialNumber { get; set; }
        public string Item { get; set; }
        public int quantity { get; set; }
        public decimal PriceBox { get; set; }
        public decimal TotalPrice { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Box> boxes = new List<Box>();

            string line = Console.ReadLine();

            while (line != "end")
            {
                string[] data = line.Split();

                string serialNumber = data[0];
                string itemName = data[1];
                int itemQuantity = int.Parse(data[2]);
                decimal itemPrice = decimal.Parse(data[3]);

                Box box = new Box();

                box.SerialNumber = serialNumber;
                box.Item = itemName;
                box.quantity = itemQuantity;
                box.PriceBox = itemPrice;
                box.TotalPrice = itemQuantity * itemPrice;

                boxes.Add(box);

                line = Console.ReadLine();

            }

            List<Box> sortedBox = boxes.OrderByDescending(boxes => boxes.TotalPrice).ToList();


            foreach (Box box in sortedBox)
            {
                Console.WriteLine($"{box.SerialNumber}");
                Console.WriteLine($"-- {box.Item} - ${box.PriceBox:f2}: {box.quantity}");
                Console.WriteLine($"-- ${box.TotalPrice:f2}");
            }
        }
    }
}
