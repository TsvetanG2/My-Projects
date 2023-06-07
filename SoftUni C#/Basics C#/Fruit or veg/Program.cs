using System;

namespace Fruit_or_veg
{
    class Program
    {
        static void Main(string[] args)
        {
            string food = Console.ReadLine();

            switch (food)
            {
                case "banana":
                case "apple":
                case "kiwi":
                case "cherry":
                case "grapes":
                case "lemon":
                    Console.WriteLine("fruit");
                    break;
                case "tomato":
                case "cucumber":
                case "carrot":
                case "pepper":
                    Console.WriteLine("vegetable");
                    break;
                default:
                    Console.WriteLine("unknown");
                    break;
      
            }
            

            
        }
    }
}
