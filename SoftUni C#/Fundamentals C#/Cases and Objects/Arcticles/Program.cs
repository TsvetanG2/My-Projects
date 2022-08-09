using System;

namespace Arcticles
{
    class Program
    {
        static void Main(string[] args)
        {
            var newArcitcle = new Arcticle(title: "some title", content: "some content",author: "some author");

            Console.WriteLine(newArcitcle);
            
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
        public  string Title { get; set;}

        public string Content { get; set;}

        public string Author { get; set;}

        public void ChangeAuthor(string author) => Author = author;

        public void Edit(string content) => Content = content;

        public void Rename(string title) => Title = title;


        public override string ToString() => $"{Title} - {Content}. {Author}";
    }
    
    
}
