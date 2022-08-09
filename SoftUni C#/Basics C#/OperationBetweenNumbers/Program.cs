using System;

namespace OperationBetweenNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int N1 = int.Parse(Console.ReadLine());
            int N2 = int.Parse(Console.ReadLine());
            string symbol = Console.ReadLine();

            double result = 0;
            bool IsSymbolValid = symbol == "/" || symbol == "%";
            bool IsResultValid = result == 0;

            switch (symbol)
            {
                case "+":
                    result = N1 + N2;
                    if (result % 2 == 0)
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - even");
                    }
                    else
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - odd");
                    }
                    break;
                case "-":
                    result = N1 - N2;
                    if (result % 2 == 0)
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - even");
                    }
                    else
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - odd");
                    }
                    break;
                case "*":
                    result = N1 * N2;
                    if (result % 2 == 0)
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - even");
                    }
                    else
                    {
                        Console.WriteLine($"{N1} {symbol} {N2} = {result} - odd");
                    }
                    break;
                case "/":
                    if ( N2 == 0)
                    {
                        Console.WriteLine($"Cannot divide {N1} by zero");
                    }
                    else
                    {
                        result = N1 / (double)N2;
                        Console.WriteLine($"{N1} {symbol} {N2} = {result:f2}");
                    }
                    break;
                case "%":
                    if (N2 == 0)
                    {
                        Console.WriteLine($"Cannot divide {N1} by zero");
                    }
                    else
                    {
                        result = N1 % N2;
                        Console.WriteLine($"{N1} {symbol} {N2} = {result:f2}");
                    }
                    break;
                default:
                    result = 0;
                    break; 
            }
            
         }
    }
}
