using System;

namespace Пресмятане_на_аквариум
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = double.Parse(Console.ReadLine());
            double b = double.Parse(Console.ReadLine());
            double c = double.Parse(Console.ReadLine());
            double percentage = double.Parse(Console.ReadLine());

            double measurments = a * b * c;
            double litres = measurments * 0.001;
            double resultperc = percentage * 1 / 100;
            double finalresult = litres * (1 - resultperc);

            Console.WriteLine(finalresult);
        }
    }
}
