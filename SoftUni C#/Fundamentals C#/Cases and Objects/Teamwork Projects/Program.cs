using System;
using System.Collections.Generic;
using System.Linq;

namespace Teamwork_Projects
{
    class Program
    {
        static void Main(string[] args)
        {
            int countOfTeamToBeCreated = int.Parse(Console.ReadLine());
            var teams = new List<Team>();

            for(int i = 0; i < countOfTeamToBeCreated; i++)
            {
                var currTeamInfo = Console.ReadLine().Split('-');
                var creator = currTeamInfo[0];
                var teamName = currTeamInfo[1];

                if (teams.Any(currTeam => currTeam.Name == teamName))
                {
                    Console.WriteLine($"Team {teamName} was already created!");
                }
                else if (teams.Any(CurrUsser => CurrUsser.Creator == creator))
                {
                    Console.WriteLine($"{creator} cannot create another team!");
                }
                else
                {
                    var team = new Team();
                    team.Name = teamName;
                    team.Creator = creator;
                    team.Members = new List<string>();
                    teams.Add(team);
                    Console.WriteLine($"Team {teamName} has been created by {creator}!");
                }
            }

            var line = Console.ReadLine();
            while (line != "end of assignment")
            {
                var membersinfo = line.Split(new string[] { "->" }, StringSplitOptions.None);
                var membername = membersinfo[0];
                var teamToJoin = membersinfo[1];

                if (teams.Any(team => team.Members.Contains(membername)) || teams.Any(creator => creator.Creator == membername))
                {
                    Console.WriteLine($"Member {membername} cannot join team {teamToJoin}!");
                }
                else if (!teams.Any(team => team.Name == teamToJoin))
                {
                    Console.WriteLine($"Team {teamToJoin} does not exist!");
                }
                else
                {
                    var currentteam = teams.Find(team => team.Name == teamToJoin);
                    currentteam.Members.Add(membername);
                }
                line = Console.ReadLine();
            }
            var completedteams = teams.Where(x => x.Members.Count > 0);
            // всички завършени отбори(направени)


            var disbannedteams = teams.Where(team => team.Members.Count == 0);
            // екипи които ще бъдат премахнати

            foreach (var team in completedteams.OrderByDescending(x => x.Members.Count).ThenBy(y => y.Name))
            {
                Console.WriteLine($"{team.Name}");
                Console.WriteLine($"- {team.Creator}");
                foreach (var member in team.Members.OrderBy(x => x))
                {
                    Console.WriteLine($"-- {member}");
                }
            }

            Console.WriteLine($"Teams to disband:");
            foreach (var disbannedteam in disbannedteams.OrderBy(x => x.Name))
            {
                Console.WriteLine($"{disbannedteam.Name}");
            }
        }
    }

    class Team
    {
        public string Name { get; set; }
        public string Creator { get; set; }
        public List<string> Members { get; set; }
    }
}
