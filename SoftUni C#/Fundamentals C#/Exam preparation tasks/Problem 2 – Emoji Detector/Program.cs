﻿using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace Problem_2___Emoji_Detector
{
    class Program
    {
        static void Main(string[] args)

        // Link task: https: //softuni .bg/trainings/resources/officedocument/71635/exam-preparation-problems-description-programming-fundamentals-with-csharp-may-2022/3729
        {
            Console.WriteLine("Insert text with *emojies*");
            string text = Console.ReadLine();

            string patternEmoji = @"(\*{2}|:{2})(?<emoji>[A-Z][a-z]{2,})\1";
            string patternNumbers = @"\d";

            MatchCollection emojiMatches = Regex.Matches(text, patternEmoji);
            MatchCollection numberMatches = Regex.Matches(text, patternNumbers);

            long threshold = 1;

            foreach (Match number in numberMatches)
            {
                threshold *= int.Parse(number.Value);
            }

            Console.WriteLine($"Cool threshold: {threshold}");
            Console.WriteLine($"{emojiMatches.Count} emojis found in the text. The cool ones are:");

            foreach (Match CoolEmoji in emojiMatches)
            {
                string emoji = CoolEmoji.Groups["emoji"].Value;
                long emojiThreshold = emoji.ToCharArray().Sum(c => c);
                // long е за дълга или голяма сума


                if (emojiThreshold >= threshold)
                {
                    Console.WriteLine(CoolEmoji.Value);
                }
            }
        }
    }
}
