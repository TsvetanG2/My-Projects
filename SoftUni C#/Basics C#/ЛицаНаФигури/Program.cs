using System;

namespace ЛицаНаФигури
{
    class Program
    {
        static void Main(string[] args)
        {
            string a = Console.ReadLine();   
            double area = 0;
           

            if ( a == "square")
            {
                double b = double.Parse(Console.ReadLine());
                area = b * b;
            }
            else if ( a == "triangle")
            {
                double c = double.Parse(Console.ReadLine());
                double h = double.Parse(Console.ReadLine());
                area = c * h / 2;
            }
            else if (a == "circle")
            {
                double r = double.Parse(Console.ReadLine());
                area = r * r * Math.PI;
            }
            else if ( a =="rectangle")
            {
                double i = double.Parse(Console.ReadLine());
                double o = double.Parse(Console.ReadLine());
                area = i * o;
            }
            if ( area !=0)
            {
                Console.WriteLine($"{area:f3}");
            }
            else
            {
                Console.WriteLine("Area is zero, or invalid figure type");
            }
        }
    }
}
