using System;

namespace WordLenght
{
    class Program
    {
        static void Main(string[] args)
        {
            string word = Console.ReadLine();

            for (int i = 0; i < word.Length; i++)
            {
                char letter = word[i];
                Console.WriteLine(letter);
            }
        }
    }
}
