using System;

namespace HomeSwitch
{
    class Program
    {
        static void Main(string[] args)
        {
            string flowers = Console.ReadLine();
            int quantity = int.Parse(Console.ReadLine());
            int budget = int.Parse(Console.ReadLine());

            double singleprice = 0;
            double totalprice = 0;

            switch (flowers)
            {
                case "Roses":
                    singleprice = 5;
                    totalprice = singleprice * quantity;

                    if (quantity > 80)
                    {
                        totalprice *= 0.10;
                    }
                    break;
                case "Dahlias":
                    singleprice = 3.80;
                    totalprice = singleprice * quantity;

                    if (quantity > 90) 
                    {
                        totalprice *= 0.15;
                    }
                    break;
                case "Tulips":
                    singleprice = 2.80;
                    totalprice = singleprice * quantity;

                    if (quantity > 80)
                    {
                        totalprice *= 0.15;
                    }
                    break;
                case "Narcisuss":
                    singleprice = 3;
                    totalprice = singleprice * quantity;

                    if (quantity < 120)
                    {
                        totalprice *= 1.15;
                    }
                    break;
                case "Gladiolus":
                    singleprice = 2.50;
                    totalprice = singleprice * quantity;

                    if (quantity < 80)
                    {
                        totalprice *= 1.20;
                    }
                    break;
            }
            if (budget >= totalprice)
            {
                double remaining = budget - totalprice;
                Console.WriteLine($"Hey you have a great garden with {quantity} {flowers} and {remaining:F2} leva left.");
            }
            else if (totalprice > budget)
            {
                double insufficient = totalprice = budget;
                Console.WriteLine($"Not enough money, you need {insufficient:F2} leva more.");

            }
            else
            {

            }
        }
    }
}
