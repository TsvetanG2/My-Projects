using System;

namespace KingVsKong
{
    class Program
    {
        static void Main(string[] args)
        {
            //Вход
            double a = double.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());
            double c = double.Parse(Console.ReadLine());

            // Уравнения 
            double decor = a * 10 / 100;
            double clothes = b * c;
            double price = decor + clothes;

            // Решение
            if (b < 150)
            {
                double final2 = a - price;

                Console.WriteLine("Action!");
                Console.WriteLine($"Wingard starts filming with {final2:f2} leva left.");
            }
            else if (b > 150)
            {
                clothes = clothes - (clothes * 10 / 100);
                double totalprice = decor + clothes;
                double finalprice = a - totalprice;

                if (totalprice > a)
                {
                    double final2 = totalprice - a;

                    Console.WriteLine("Not enough money!");
                    Console.WriteLine($"Wingard needs {final2:f2} leva more.");
                }
                else
                {
                    Console.WriteLine("Action!");
                    Console.WriteLine($"Wingard starts filming with {finalprice:f2} leva left.");
                }
            }     
        }
    }
}

