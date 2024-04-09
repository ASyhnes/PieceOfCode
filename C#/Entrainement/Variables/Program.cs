using System;
using System.IO;

namespace Variables
{
    class Program
    {
        

        //fonctions
        static void Main(string[] args) 
        {
            //variables
            string name;
            int age;
            float score;

            name = "Anthony";
            Console.WriteLine("Hello " + name);
            name = name + "Jeanjean";
            Console.WriteLine(" Heallo " + name);
            age = int.Parse(Console.ReadLine());
            Console.WriteLine("Age = " + age);
        }
    }
}