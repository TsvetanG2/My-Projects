using System;

namespace Lunch_Break
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = Console.ReadLine();
            int episode = int.Parse(Console.ReadLine());
            int breakduration = int.Parse(Console.ReadLine());

            int lunchbreak = breakduration * 1 / 8;
            int coffeebreak = breakduration * 1 / 4;
            int timeleft = breakduration - lunchbreak - coffeebreak;
            int timeleft2 = timeleft - episode;
            int timeneeded = episode - timeleft;


            if (timeleft >= episode)
            {
                timeleft++;
                Console.WriteLine($"You have enough time to watch {name} and left with {timeleft2} minutes free time.");
            }
            else
            {
                timeneeded++;
                Console.WriteLine($"You don't have enough time to watch {name}, you need {timeneeded} more minutes.");
            }
        }
    }
}
