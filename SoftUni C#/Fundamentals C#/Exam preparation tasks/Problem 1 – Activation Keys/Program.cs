﻿using System;

namespace Problem_1___Activation_Keys
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Key Generator");
            Console.WriteLine("Example: asdfghjklasdfghjjllasd");

            string key = Console.ReadLine();

            Console.WriteLine("You have 3 commands: Contains, Flip and Slice");

            while (true)
            {
                string command = Console.ReadLine();

                if (command == "Generate")
                {
                    break;
                }
                string[] tokens = command.Split(">>>", StringSplitOptions.RemoveEmptyEntries);

                string action = tokens[0];

                switch (action)
                {
                    case "Contains":
                        // tokens[1] ще ни бъди substring
                        Contains(tokens[1], key);
                        break;
                    case "Flip":
                        key = Flip(tokens[1], int.Parse(tokens[2]), int.Parse(tokens[3]), key);
                        break;
                    case "Slice":
                        key = Slice(int.Parse(tokens[1]), int.Parse(tokens[2]), key);
                        break;
                
                }
            }
            Console.WriteLine($"Your activation key is: {key}");
        }

        private static string Slice(int startindex, int endindex, string key)
        {
            key = key.Remove(startindex, endindex - startindex);

            Console.WriteLine(key);

            return key;
        }

        static string Flip(string casing, int startindex, int endindex, string key)
        {
            string originalSubstring = key.Substring(startindex, endindex - startindex);

            string newSubstring = originalSubstring.ToLower(); // Всички главни букви ше ги направи на малки
            
            if (casing == "Upper")
            {
                newSubstring = newSubstring.ToUpper(); // При условие че трябва да са с главни букви
                // ще ги направи с главни букви
            }

            key = key.Replace(originalSubstring, newSubstring);

            Console.WriteLine(key);

            return key;
        }

        static void Contains(string substring, string key)
        {
            if (key.Contains(substring))
            {
                Console.WriteLine($"{key} contains {substring}");
            }
            else
            {
                Console.WriteLine($"Substring not found!");
            }
        }
    }
}
