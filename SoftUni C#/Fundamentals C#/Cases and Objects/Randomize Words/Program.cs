﻿using System;

namespace Randomize_Words
{
    class Program
    {
        static void Main(string[] args)
        {
           string[] words = Console.ReadLine().Split(' ');

            Random random = new Random();

            for(int i = 0; i < words.Length; i++)
            {
                int randomIndex = random.Next(0, words.Length);
                string currentWord = words[i];
                words[i] = words[randomIndex];
                words[randomIndex] = currentWord;
            }
            
            foreach (string word in words)
            {
                Console.WriteLine(word);
            }

            
        }
    }
}
