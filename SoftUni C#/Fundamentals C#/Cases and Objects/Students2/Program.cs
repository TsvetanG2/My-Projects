using System;
using System.Collections.Generic;
using System.Linq;

namespace Students2
{
    class Program
    {
        static void Main(string[] args)
        {
            int countofStudents = int.Parse(Console.ReadLine());
            List<Student> students = new List<Student>();

            for (int i =0; i < countofStudents; i++)
            {
                string[] currStudentInfo = Console.ReadLine().Split(separator: ' ');
                var student = new Student(firstName: currStudentInfo[0],lastName: currStudentInfo[1], double.Parse(currStudentInfo[2]));
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

        public Student(string firstName,string lastName, double grade)
        {
            FirstName = firstName;
            LastName = lastName;
            Grade = grade;
        }
        public string FirstName { get; set; }

        public string LastName { get; set; }

        public double Grade { get; set; }
    }
}
