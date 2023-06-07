using System;

namespace TaskUni2
{
    class Program
    {
        static void Main(string[] args)
        {
            double grade = double.Parse(Console.ReadLine());


            if (grade >= 5.0)
            { 
                Console.WriteLine("Excellent");
            }
            if (grade <= 4.0)
            {
                Console.WriteLine("You did good");
            }

            else
            {
                Console.WriteLine("You could do better");
            }





        }



    }
}
            
