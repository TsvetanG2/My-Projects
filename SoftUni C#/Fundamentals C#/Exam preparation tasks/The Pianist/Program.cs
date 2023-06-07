using System;
using System.Collections.Generic;

namespace The_Pianist
{
    class Program
    {
        static void Main(string[] args)
        // Линк към задачата
        // https ://softuni .bg /trainings/resources/officedocument/71634/exam-preparation-problems-description-programming-fundamentals-with-csharp-may-2022/3729
        {
            int numberOfLines = int.Parse(Console.ReadLine());

            //трябва ни dictionary където ще добавим нашето парче
            // парче в което да има Dictionary и ще пазим неговото Value : Key
            var music = new Dictionary<string, KeyValuePair<string, string>>();
            var order = new List<string>();
            //Трябва да напълним текущият ни вход
            for (int i = 0; i < numberOfLines; i++)
            {
                var pieceInfo = Console.ReadLine().Split("|", StringSplitOptions.RemoveEmptyEntries);
                // Fur Elise
                string piece = pieceInfo[0];
                // Bethoven
                string composer = pieceInfo[1];
                //A minor 
                string key = pieceInfo[2];

                if (!music.ContainsKey(piece))
                {
                    // Dictionary e двойка от KeyValuePair
                    // Използваме KeyValuePair защото с Dictionary не става
                    // Ще използваме композитора и ключа към него, който носи стойност
                    music.Add(piece, new KeyValuePair<string, string>(composer, key));
                    order.Add(piece);
                }
            }

            string commands = Console.ReadLine();
            while (commands != "Stop")
            {
                // Add Sonata No,2  Chopin  B Minor
                string[] command = commands.Split("|");
                // piece = Sonata No,2  което ни е command[1]
                string piece = command[1];
                // comand[0] ще бъдат Add, ChangeKey, Remove
                switch (command[0])
                {
                    case "Add":
                        {
                            //command[2] се пада нашият композитор => Пример: Chopin
                            string composer = command[2];
                            //comand[3] се пада нашичт ключ => B Minor
                            string key = command[3];

                            if (!music.ContainsKey(piece))
                            {
                                music.Add(piece, new KeyValuePair<string, string>(composer, key));
                                Console.WriteLine($"{piece} by {composer} in {key} added to the collection!");
                                order.Add(piece);
                            }
                            else
                            {
                                Console.WriteLine($"{piece} is already in the collection!");
                            }

                            break;
                        }
                    case "Remove":
                        {
                            if (music.ContainsKey(piece))
                            {
                                music.Remove(piece);
                                Console.WriteLine($"Successfully removed {piece}!");
                                order.Remove(piece);
                            }
                            else
                            {
                                Console.WriteLine($"Invalid operation! {piece} does not exist in the collection.");
                            }
                            break;
                        }
                    case "ChangeKey":
                        {
                            string newKey = command[2];
                            // Искаме да направим проверка ако парчето съществува в колекцията
                            // Ако да, искаме да вземем неговите данни, композитора, който има ключа
                            if (music.ContainsKey(piece))
                            {
                                var pieceData = music[piece];
                                var composer = pieceData.Key;
                                // Искаме да сменим неговата стойност и да добавим новата стойност с новият композитор
                                // който имаме
                                music[piece] = new KeyValuePair<string, string>(composer, newKey);
                                Console.WriteLine($"Changed the key of {piece} to {newKey}!");
                            }
                            else
                            {

                                Console.WriteLine($"Invalid operation! {piece} does not exist in the collection.");
                            }
                            break;
                        }
                }

                commands = Console.ReadLine();
            }
            // Имената на всички парчета, които имаме
            foreach (var pieces in order)
            {
                // music[pieces].Key държи нашият композитор / composer
                // music[pieces].Value държи нашият ключ / key
                Console.WriteLine($"{pieces} -> Composer: {music[pieces].Key}, Key: {music[pieces].Value}");
            }
        }
    }
}
