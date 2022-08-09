using System;

namespace GuessThePassword
{
    class Program
    {
        static void Main(string[] args)
        {
            string password = (Console.ReadLine());
            string a = "s3cr3t!P@ssw0rd";


            if (password == a)
            {
                Console.WriteLine("Welcome");
            }
            else
            {
                Console.WriteLine("Wrong password!");
            }
        }
    }
}
