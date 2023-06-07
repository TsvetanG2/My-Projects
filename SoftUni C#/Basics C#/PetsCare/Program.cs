using System;

namespace PetsCare
{
    class Program
    {
        static void Main(string[] args)
        {
            int foodbought = int.Parse(Console.ReadLine());

            string command = "";
            int foodingrams = foodbought * 1000;

            bool isFoodFinished = false;

            while (true)
            {
                command = Console.ReadLine();

                if (command == "Adopted")
                {
                    break;
                }

                int gramseaten = int.Parse(command);
                foodingrams -= gramseaten;

                if (foodingrams <= gramseaten)
                {
                    isFoodFinished = true;
                }

            }
            if (isFoodFinished)
            {
                Console.WriteLine($"Food is not enough. You need {Math.Abs(foodingrams)} grams more.");
            }
            else
            {
                Console.WriteLine($"Food is enough! Leftovers: {Math.Abs(foodingrams)} grams.");
            }



        }
    }
}
