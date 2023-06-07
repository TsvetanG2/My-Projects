using System;

namespace Calculator_of_evaluation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Insert the total amount of points you have in the exam");
            Console.WriteLine("For example: if 60/100, type only 60");
            double score = int.Parse(Console.ReadLine());
            Console.WriteLine("Insert the total amount of points in the exam");
            double pointInExam = int.Parse(Console.ReadLine());
            double result = (score / pointInExam) * 6;
            Console.WriteLine($"Your evaluation/ score is: {result:f2}");
        }
    }
}
