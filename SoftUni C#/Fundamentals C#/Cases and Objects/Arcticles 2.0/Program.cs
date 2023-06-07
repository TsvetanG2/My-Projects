using System;

namespace Arcticles
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] currentArcticle = Console.ReadLine().Split(separator: ", ");
            var arcticle = new Arcticle(title: currentArcticle[0], content: currentArcticle[1], author: currentArcticle[2]);

            int CountOfChanges = int.Parse(Console.ReadLine());

            for (int i = 0; i < CountOfChanges; i++)
            {
                string[] lines = Console.ReadLine().Split(separator: ": ");
                string command = lines[0];
                string comment = lines[1];

                switch (command)
                {

                    case "Edit":
                        arcticle.Edit(comment);
                        break;
                    case "ChangeAuthor":
                        arcticle.ChangeAuthor(comment);
                        break;
                    case "Rename":
                        arcticle.Rename(comment);
                        break;

                }

            }
            Console.WriteLine(arcticle);

            //var newArcitcle = new Arcticle(title: "some title", content: "some content", author: "some author");

            // Console.WriteLine(newArcitcle);
            // newArcitcle.Edit(content: "better content");
            // newArcitcle.ChangeAuthor(author: "better author");
            // newArcitcle.Rename(title: "better title");

        }
    }

    class Arcticle
    {

        public Arcticle(string title, string content, string author)
        {
            Author = author;
            Title = title;
            Content = content;
        }
        public string Title { get; set; }

        public string Content { get; set; }

        public string Author { get; set; }

        public void ChangeAuthor(string author) => Author = author;

        public void Edit(string content) => Content = content;

        public void Rename(string title) => Title = title;


        public override string ToString() => $"{Title} - {Content}: {Author}";
    }


}
