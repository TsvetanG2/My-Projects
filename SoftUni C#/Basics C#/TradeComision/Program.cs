using System;

namespace TradeComision
{
    class Program
    {
        static void Main(string[] args)
        {
            string town = Console.ReadLine();
            double sales = double.Parse(Console.ReadLine());

            bool IsCityValid = town == "Sofia" || town == "Plovdiv" || town == "Varna";
            bool isSaleValid = sales >= 0;

            if (!(IsCityValid) || !isSaleValid)
            {
                Console.WriteLine("error");
            }
            double result = 0;
            if (town == "Sofia")
            {
                if (sales >= 0 && sales <= 500)
                {
                    result = sales * 0.05;
                }
                else if (sales > 500 && sales <= 1000)
                {
                    result = sales * 0.07;
                }
                else if (sales > 1000 && sales <= 10000)
                {
                    result = sales * 0.08;
                }
                else if (sales > 10000)
                {
                    result = sales * 0.12;
                }
                Console.WriteLine($"{result:F2}");
            }
            else if (town == "Varna")
            {
                if (sales >= 0 && sales <= 500)
                {
                    result = sales * 0.045;
                }
                else if (sales > 500 && sales <= 1000)
                {
                    result = sales * 0.075;
                }
                else if (sales > 1000 && sales <= 10000)
                {
                    result = sales * 0.10;
                }
                else if (sales > 10000)
                {
                    result = sales * 0.13;
                }
                Console.WriteLine($"{result:F2}");
            }
            else if (town == "Plovdiv")
            {
                if (sales >= 0 && sales <= 500)
                {
                    result = sales * 0.055;
                }
                else if (sales > 500 && sales <= 1000)
                {
                    result = sales * 0.08;
                }
                else if (sales > 1000 && sales <= 10000)
                {
                    result = sales * 0.12;
                }
                else if (sales > 10000)
                {
                    result = sales * 0.145;
                }
                Console.WriteLine($"{result:F2}");
            }
            Console.WriteLine();        
        }
    }
}
