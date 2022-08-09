using System;
using System.Collections.Generic;
using System.Linq;

namespace StudentsMadeByMe
{
    class Program
    {
        static void Main(string[] args)
        {
            int countofStudents = int.Parse(Console.ReadLine());
            List<Student> students = new List<Student>();

            for (int i = 0; i < countofStudents; i++)
            {
                string[] currStudentInfo = Console.ReadLine().Split(separator: ' ');
                var student = new Student(firstname: currStudentInfo[0], secondname: currStudentInfo[1], double.Parse(currStudentInfo[2]));
                students.Add(student);
            }
            students = students.OrderByDescending(currStudent => currStudent.Grade).ToList();

            foreach (var student in students)
            {
                Console.WriteLine($"{student.FirstName} {student.LastName}: {student.Grade:f2}");
            }
        }
    }

    class Student
    {
        public Student(string firstname, string secondname, double grade)
        {
            FirstName = firstname;
            LastName = secondname;
            Grade = grade;
        }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public double Grade { get; set; }
    }
}
