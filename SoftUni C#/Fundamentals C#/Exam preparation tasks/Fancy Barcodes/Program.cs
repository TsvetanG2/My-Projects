using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace Fancy_Barcodes
{
    class Program
    {
        static void Main(string[] args)
        // Вход:
        //3
        //@#FreshFisH@#
        //@###Brea0D@###
        //@##Che4s6E@##

        // Изход:
        //
        //Product group: 00
        //Product group: 0
        //Product group: 46

        {
            // Баркода е взет от regex101.com , като се вкарва информацията за баркодовете
            // които са дадени в условието
            string barcodePattern = @"@#+[A-Z][a-zA-Z\d]{4,}[A-Z]@#+";

            int numberOfBarcodesToReceive = int.Parse(Console.ReadLine());

            for (int i = 0; i < numberOfBarcodesToReceive; i++)
            {
                string CurrentBarcode = Console.ReadLine();

                // Проверяваме дали имаме съвпадение
                if (Regex.IsMatch(CurrentBarcode, barcodePattern)) // Ще ги сравни дали си съвпадат, тоест ше върне true или false
                {
                    // Примерно получаваме @###Bread0@### => В него имаме => B R E A D => искаме да вземем само нулата
                    // Втори Пример @###Che46sE@### => C H E 4 6 S E => 46 - Искаме да вземем само цифрите
                    //Как можем да ги вземем?
                    //С char масив
                    char[] digits = CurrentBarcode.Where(char.IsDigit).ToArray();
                    // digits => [4, 6] (Cheese)

                    // Взимаме дължината на нашият масив
                    // А ако няма числа то пример: @#FreshFisH@# => digits.Lenght = 0
                    string barcodeGroup = digits.Length == 0 ? "00" : string.Join(
                        "", digits); // [4,6] => 46
                    Console.WriteLine($"Product group: {barcodeGroup}");
                }
                else
                {
                    Console.WriteLine("Invalid barcode");
                }
            }
        }
    }
}
