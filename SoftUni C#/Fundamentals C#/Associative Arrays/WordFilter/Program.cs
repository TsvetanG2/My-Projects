using System;
using System.Linq;

namespace WordFilter
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().Split();

            string[] evelLengthWords = words.Where(word => word.Length % 2 == 0).ToArray();

            Console.WriteLine(string.Join(Environment.NewLine, evelLengthWords));
        }
    }
}
