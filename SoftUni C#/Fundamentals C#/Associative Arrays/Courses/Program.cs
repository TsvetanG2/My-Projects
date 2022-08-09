using System;
using System.Collections.Generic;

namespace Courses
{
    class Program
    {
        static void Main(string[] args)
        {
            var nestDictionary = new Dictionary<Dictionary<string, string>,
                Dictionary<string, string>>();

            var keyDictionary = new Dictionary<string, string>();
            keyDictionary.Add("name", "pesho");
            var valueDictionary = new Dictionary<string, string>();
            valueDictionary.Add("value", "pesho");
            nestDictionary.Add(keyDictionary, valueDictionary);
            Console.WriteLine(nestDictionary[keyDictionary] = valueDictionary);

            foreach (var nestdictionary in nestDictionary )
            {
                Console.WriteLine(nestdictionary.Key);
                foreach (var kvpDictionary in nestdictionary.Value)
                {
                    Console.WriteLine(kvpDictionary.Key);
                    Console.WriteLine(kvpDictionary.Value);
                }
                Console.WriteLine(nestdictionary.Value);
            }
        }
    }
}
