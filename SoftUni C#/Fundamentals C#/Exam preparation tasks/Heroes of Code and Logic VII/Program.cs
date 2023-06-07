using System;
using System.Collections.Generic;

namespace Heroes_of_Code_and_Logic_VII
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<int>> heroes = new Dictionary<string, List<int>>();

            int count = int.Parse(Console.ReadLine());

            for (int i = 0; i < count; i++)
            {
                string[] hereosProperties = Console.ReadLine().Split(" ", StringSplitOptions.RemoveEmptyEntries);

                string name = hereosProperties[0];
                int hitPoints = int.Parse(hereosProperties[1]);
                int manaPoints = int.Parse(hereosProperties[2]);

                if (!heroes.ContainsKey(name))
                {
                    heroes.Add(name, new List<int>());
                }
                // Създава се нов списък и индексите се променят
                heroes[name].Add(hitPoints); // ударите ще са на индекс 0
                heroes[name].Add(manaPoints); // маната ще е на индекс 1
            }

            while (true)
            {
                string command = Console.ReadLine();

                if (command == "End")
                {
                    break;

                }

                string[] tokens = command.Split(" - ", StringSplitOptions.RemoveEmptyEntries);
                string action = tokens[0];
                switch(action)
                {
                    case "CastSpell":
                        CastSpell(tokens[1], int.Parse(tokens[2]), tokens[3], heroes);
                        break;
                    case "TakeDamage":
                        TakeDamage(tokens[1], int.Parse(tokens[2]),tokens[3], heroes);
                        break;
                    case "Recharge":
                        Recharge(tokens[1], int.Parse(tokens[2]), heroes);
                        break;
                    case "Heal":
                        Heal(tokens[1], int.Parse(tokens[2]), heroes);
                        break;

                }

            }

            foreach (var hero in heroes)
            {
                Console.WriteLine(hero.Key);
                Console.WriteLine($" HP: {hero.Value[0]}");
                Console.WriteLine($" MP: {hero.Value[1]}");
            }
        }

        static void CastSpell(string name, int manaNeeded, string spell, Dictionary<string, List<int>> heroes)
        {
            if (heroes[name][1] >= manaNeeded)
            {
                heroes[name][1] -= manaNeeded;

                Console.WriteLine($"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!");
            }
            else
            {
                Console.WriteLine($"{name} does not have enough MP to cast {spell}!");
            }
        }

         static void TakeDamage(string name, int damage, string attacker, Dictionary<string, List<int>> heroes)
        {
            heroes[name][0] -= damage;
            if (heroes[name][0] > 0)
            {
                Console.WriteLine($"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!");
            }
            else
            {
                Console.WriteLine($"{name} has been killed by {attacker}!");
                heroes.Remove(name);
            }
        }

         static void Recharge(string name, int mana, Dictionary<string, List<int>> heroes)
        {
            int originalMana = heroes[name][1];
            heroes[name][1] += mana;
            if (heroes[name][1] > 200)
            {
                heroes[name][1] = 200;
            }
            Console.WriteLine($"{name} recharged for {heroes[name][1] - originalMana} MP!");
        }

         static void Heal(string name, int heal, Dictionary<string, List<int>> heroes)
        {
            int originalHeal = heroes[name][0];
            heroes[name][0] += heal;
            if (heroes[name][0] > 100)
            {
                heroes[name][0] = 100;
            }
            Console.WriteLine($"{name} healed for {heroes[name][0] - originalHeal} HP!");
        }
    }
}
