using System;
using System.Collections.Generic;
using System.Linq;

namespace List_Manipulation_Basics
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();

            while (true)
            {
                string command = Console.ReadLine();

                if (command == "end")
                {
                    break;
                }
                string[] tokens = command.Split();
                string action = tokens[0];

                switch (action)
                {

                    case "Add":
                        int numberToAdd = int.Parse(tokens[1]);
                        numbers.Add(numberToAdd);
                        break;
                    case "Remove":
                        int numberToRemove = int.Parse(tokens[1]);
                        numbers.Remove(numberToRemove);
                        break;
                    case "RemoveAt":
                        int indexToRemove = int.Parse(tokens[1]);
                        numbers.RemoveAt(indexToRemove);
                        break;
                    case "Insert":
                        int numberToInsert = int.Parse(tokens[1]);
                        int IndexToInsert = int.Parse(tokens[2]);
                        numbers.Insert(IndexToInsert, numberToInsert);
                        break;
                }
            }
            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
