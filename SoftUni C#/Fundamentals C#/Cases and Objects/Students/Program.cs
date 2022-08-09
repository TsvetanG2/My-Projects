using System;
using System.Linq;
using System.Collections.Generic;


namespace ObjectsAndClasses
{
    class MainClass
    {
        public static void Main()
        {
            var listOfStudents = new List<Student>();

            string command = Console.ReadLine();
            while (command != "end")
            {
                string[] commandArrguments = command.Split();
                string firstName = commandArrguments[0];
                string lastName = commandArrguments[1];
                string age = commandArrguments[2];
                string city = commandArrguments[3];

                Student student = listOfStudents
                    .FirstOrDefault(s => s.FirstName == firstName && s.LastName == lastName);

                //bool fistNameExist = listOfStudents.Exists(s => s.FirstName.Contains(firstName));
                //bool lastNameExist = listOfStudents.Exists(s => s.LastName.Contains(lastName));
                if (student != null)
                {
                    //var firstRepitableIndex = listOfStudents.IndexOf(student);
                    //listOfStudents.RemoveAt(firstRepitableIndex);
                    student.FirstName = firstName;
                    student.LastName = lastName;
                    student.Agee = age;
                    student.City = city;
                }
                else
                {
                    student = new Student();
                    student.FirstName = firstName;
                    student.LastName = lastName;
                    student.Agee = age;
                    student.City = city;
                    listOfStudents.Add(student);
                }

                command = Console.ReadLine();
            }

            string filteredCity = Console.ReadLine();
            List<Student> FilteredStudent = listOfStudents.Where(s => s.City == filteredCity).ToList();
            foreach (var student in FilteredStudent)
            {
                Console.WriteLine($"{student.FirstName} {student.LastName} is {student.Agee} years old.");
            }
        }
    }

    public class Student
    {
        public string FirstName { get; set; }

        public string LastName { get; set; }

        public string Agee { get; set; }

        public string City { get; set; }
    }
}
