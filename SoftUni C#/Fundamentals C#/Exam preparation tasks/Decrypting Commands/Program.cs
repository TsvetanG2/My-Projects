using System;

namespace Nikulden_s_Charity
{
    class Program
    {
        static void Main(string[] args)
        {

            string message = Console.ReadLine();
            int sumOfSubString = 0;

            while (true)
            {
                string input = Console.ReadLine();

                string[] token = input.Split(" ", StringSplitOptions.RemoveEmptyEntries);
                string command = token[0];
                if (input == "Finish")
                {
                    break;
                }
                {
                    if (command == "Replace")
                    {
                        string currentChar = token[1];
                        string newChar = token[2];

                        if (message.Contains(currentChar))
                        {
                            message = message.Replace(currentChar, newChar);
                            Console.WriteLine(message);
                        }

                    }

                    else if (command == "Cut")
                    {
                        int startIndex = int.Parse(token[1]);
                        int endIndex = int.Parse(token[2]);
                        int lengths = (endIndex - startIndex) + 1;

                        if (startIndex >= 0 && endIndex > startIndex && endIndex < message.Length)
                        {
                            message = message.Remove(startIndex, lengths);
                            Console.WriteLine(message);
                        }
                        else
                        {
                            Console.WriteLine("Invalid indices!");
                        }
                    }
                    else if (command == "Make")
                    {

                        if (token[1] == "Upper")
                        {
                            message = message.ToUpper();
                            Console.WriteLine(message);
                        }

                        else if (token[1] == "Lower")
                        {
                            message = message.ToLower();
                            Console.WriteLine(message);

                        }


                    }

                    else if (command == "Check")
                    {
                        string str = token[1];

                        if (message.Contains(str))
                        {
                            Console.WriteLine($"Message contains {str}");
                        }

                        else
                        {
                            Console.WriteLine($"Message doesn't contain {str}");
                        }

                    }

                    else if (command == "Sum")
                    {
                        long startIndex = long.Parse(token[1]);
                        long endIndex = long.Parse(token[2]);
                        long length = (endIndex - startIndex) + 1;

                        if (startIndex >= 0 && endIndex > startIndex && endIndex < message.Length)
                        {
                            string substr = message.Substring((int)startIndex, (int)length);
                            for (int i = 0; i < substr.Length; i++)
                            {
                                sumOfSubString += substr[i];
                            }
                            Console.WriteLine(sumOfSubString);
                        }
                        else
                        {
                            Console.WriteLine("Invalid indices!");
                        }
                    }
                }
            }
        }
    }
}