using System;

namespace WorldRecord
{
    class Program
    {
        static void Main(string[] args)
        {
            double recordseconds = double.Parse(Console.ReadLine());
            double metres = double.Parse(Console.ReadLine());
            double secondspermetre = double.Parse(Console.ReadLine());

            // Уравнения
            double result = metres * secondspermetre;
            double addmetre = metres / 15;
            double result2 = addmetre * 12.5;
            double result3 = result + result2;

            
            if (recordseconds < result3)
            {

                double finalresult = result3 - recordseconds;
                Console.WriteLine($"No, he failed! He was {finalresult:f2} seconds slower.");
            }
            else 
            {
                
                Console.WriteLine($"Yes, he succeeded! The new world record is {result3:f2} seconds.");
            }
        }
    }
}
