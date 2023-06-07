using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

namespace _03_MessagesManager
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> sentMessages = new Dictionary<string, int>();
            Dictionary<string, int> receivedMessages = new Dictionary<string, int>();

            int maxCapacity = int.Parse(Console.ReadLine());

            string command;
            while ((command = Console.ReadLine()) != "Statistics")
            {
                string[] commandArgs = command.Split("=").ToArray();
                string commandType = commandArgs[0];

                if (commandType == "Add")
                {
                    string username = commandArgs[1];
                    int sent = int.Parse(commandArgs[2]);
                    int received = int.Parse(commandArgs[3]);

                    if (!sentMessages.ContainsKey(username))
                    {
                        sentMessages.Add(username, sent);
                        receivedMessages.Add(username, received);
                    }
                }
                else if (commandType == "Message")
                {
                    string sender = commandArgs[1];
                    string receiver = commandArgs[2];

                    if (sentMessages.ContainsKey(sender) && sentMessages.ContainsKey(receiver))
                    {
                        sentMessages[sender] += 1;
                        receivedMessages[receiver] += 1;

                        if ((sentMessages[sender] + receivedMessages[sender]) >= maxCapacity)
                        {
                            Console.WriteLine($"{sender} reached the capacity!");
                            sentMessages.Remove(sender);
                            receivedMessages.Remove(sender);
                        }
                        if ((receivedMessages[receiver] + sentMessages[receiver]) >= maxCapacity)
                        {
                            Console.WriteLine($"{receiver} reached the capacity!");
                            sentMessages.Remove(receiver);
                            receivedMessages.Remove(receiver);
                        }
                    }

                }
                else if (commandType == "Empty")
                {
                    string username = commandArgs[1];

                    if (username == "All")
                    {
                        sentMessages.Clear();
                        receivedMessages.Clear();
                    }
                    else
                    {
                        if (sentMessages.ContainsKey(username))
                        {
                            sentMessages.Remove(username);
                            receivedMessages.Remove(username);
                        }
                    }
                }
            }
            Console.WriteLine($"Users count: {sentMessages.Count}");


            foreach (var kvp in receivedMessages.OrderBy(kvp => kvp.Key[1]).ThenByDescending(kvp => kvp.Value))
            {
                
                string user = kvp.Key;
                int receivedMessagesPerUser = kvp.Value;
                int sentMessagesPerUser = sentMessages[user];
                int sum = sentMessagesPerUser + receivedMessagesPerUser;
                Console.WriteLine($"{user} - {sum}");
            }
        }
    }
}