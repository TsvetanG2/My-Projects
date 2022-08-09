using System;

namespace ClassesAndObjects
{
    class Program
    {
        static void Main(string[] args)
        {
            Dog John = new Dog()
            {
                Name = "John",
                Age = 4,
                Breed = "Jack Russel",
                Weight = 6.1
            };

            Console.WriteLine("John's dog");
            John.PritnNameAndAge();
            Console.WriteLine();

            Dog Pesho = new Dog()
            {
                Name = "Pesho",
                Age = 6,
                Breed = "Jack Russel",
                Weight = 4.5
            };

            Console.WriteLine("Pesho's dog");
            Pesho.PritnNameAndAge();
            Console.WriteLine();
        }

        class Dog
        {
            public string Name { get; set; }

            public string Breed { get; set; }

            public int Age { get; set; }

            public double Weight { get; set; }

            public void PritnNameAndAge()
            {
                Console.WriteLine($"Name: {this.Name}, Age: {this.Age}");
            }

        }
    }
}
