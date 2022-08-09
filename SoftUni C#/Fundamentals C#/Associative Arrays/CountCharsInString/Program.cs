using System;
using System.Collections.Generic;

namespace CountCharsInString
{
    class Program
    {
        static void Main(string[] args)
        {
            char[] word = Console.ReadLine().ToCharArray(); // "text" ще изглежда = ['t','e','x','t']

            Dictionary<char, int> letters = new Dictionary<char, int>(); // charL int: => [char 't': int 2]

            foreach (var letter in word)
            {
                if (letter != ' ')
                {
                    if (!letters.ContainsKey(letter)) // letters.ContainsKey('t') - имаш ли 't'
                    {
                        letters[letter] = 0;
                    }
                    letters[letter]++; // ако имаш тази буквичка искам да добавиш 
                }
            }
            foreach (var kvpLetter in letters)
            {
                Console.WriteLine($"{kvpLetter.Key} -> {kvpLetter.Value}");
            }
        }
    }
}
