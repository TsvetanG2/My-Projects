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
            bool isListChanged = false;


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
                        isListChanged = true;
                        break;
                    case "Remove":
                        int numberToRemove = int.Parse(tokens[1]);
                        numbers.Remove(numberToRemove);
                        isListChanged = true;
                        break;
                    case "RemoveAt":
                        int indexToRemove = int.Parse(tokens[1]);
                        numbers.RemoveAt(indexToRemove);
                        isListChanged = true;
                        break;
                    case "Insert":
                        int numberToInsert = int.Parse(tokens[1]);
                        int IndexToInsert = int.Parse(tokens[2]);
                        numbers.Insert(IndexToInsert, numberToInsert);
                        isListChanged = true;
                        break;
                    case "Contains":
                        CheckContains(int.Parse(tokens[1]), numbers);
                        break;
                    case "PrintEven":
                        PrintEven(numbers);
                        break;
                    case "PrintOdd":
                        PrintOdd(numbers);
                        break;
                    case "GetSum":
                        GetSum(numbers);
                        break;
                    case "Filter":
                        FilteredNumber(tokens[1], int.Parse(tokens[2]), numbers);
                        break;
                }
            }
            if (isListChanged)
            {
                Console.WriteLine(string.Join(" ", numbers));
            }
            Console.WriteLine();
        }
        private static void FilteredNumber(string filter, int numberToFilter, List<int> numbers)
        {
            switch (filter)
            {
                case "<":

                    foreach (var number in numbers)
                    {
                        if (number < numberToFilter)
                        {
                            Console.Write($"{number} ");
                        }
                    }
                    break;
                case "<=":

                    foreach (var number in numbers)
                    {
                        if (number <= numberToFilter)
                        {
                            Console.Write($"{number} ");
                        }
                    }
                    break;
                case ">":

                    foreach (var number in numbers)
                    {
                        if (number > numberToFilter)
                        {
                            Console.Write($"{number} ");
                        }
                    }
                    break;
                case ">=":

                    foreach (var number in numbers)
                    {
                        if (number >= numberToFilter)
                        {
                            Console.Write($"{number} ");
                        }
                    }
                    break;
            }
            Console.WriteLine();
        }

        static void GetSum(List<int> numbers)
        {
            int sum = 0;
            foreach (var number in numbers)
            {
                sum += number;
            }
            Console.WriteLine(sum);
        }

        static void PrintOdd(List<int> numbers)
        {
            foreach (var number in numbers)
            {
                if (number % 2 != 0)
                {
                    Console.Write($"{number} ");
                }
                
            }
            Console.WriteLine();
        }

        static void PrintEven(List<int> numbers)
        {
            foreach (var number in numbers)
            {
                if ( number % 2== 0)
                {
                    Console.Write($"{number} ");
                }
            }
            Console.WriteLine();
        }

        static void CheckContains(int number, List<int> numbers)
        {
            if (numbers.Contains(number))
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No such number");
            }
            
        }
    }
}
