# Name: Krittitee Chaisang #  Student ID: 6810545441
class Player:
    def __init__(self, name: str, skill: int):
        self.name = name
        self.skill = skill


class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.__players: list[Player] = []

    def add_player(self, player_name: str, skill: int) -> bool:
        for p in self.__players:
            if p.name == player_name:
                return False
        self.__players.append(Player(player_name, skill))
        return True

    def remove_player(self, player_name: str) -> bool:
        for i, p in enumerate(self.__players):
            if p.name == player_name:
                del self.__players[i]
                return True
        return False

    def get_report(self) -> str:
        n = len(self.__players)
        if n == 0:
            avg = 0.0
        else:
            total = sum(p.skill for p in self.__players)
            avg = total / n
        return (
            f"--- Team Report ---\n"
            f"Team: {self.team_name}\n"
            f"Players: {n}\n"
            f"Average Skill: {avg:.1f}"
        )


def main():
    league: dict[str, Team] = {}

    while True:
        raw = input("Enter command: ").strip()
        if not raw:
            print("Error: Invalid command.")
            continue

        parts = raw.split()
        keyword = parts[0].lower()

        if keyword == "exit":
            print("Goodbye.")
            break

        if keyword == "addteam":
            if len(parts) != 2:
                print("Error: Invalid command.")
                continue
            team_name = parts[1]
            if team_name in league:
                print(f"Error: Team {team_name} already exists.")
            else:
                league[team_name] = Team(team_name)
                print(f"Team {team_name} created.")
            continue

        if keyword == "addplayer":
            if len(parts) != 4:
                print("Error: Invalid command.")
                continue
            team_name, player_name, skill_str = parts[1], parts[2], parts[3]
            try:
                skill = int(skill_str)
            except ValueError:
                print("Error: Skill must be an integer.")
                continue
            team = league.get(team_name)
            if team is None:
                print("Error: Team not found.")
                continue
            if team.add_player(player_name, skill):
                print(f"Player {player_name} added to {team_name}.")
            else:
                print(f"Error: Player {player_name} already on team.")
            continue

        if keyword == "removeplayer":
            if len(parts) != 3:
                print("Error: Invalid command.")
                continue
            team_name, player_name = parts[1], parts[2]
            team = league.get(team_name)
            if team is None:
                print("Error: Team not found.")
                continue
            if team.remove_player(player_name):
                print(f"Player {player_name} removed from {team_name}.")
            else:
                print(f"Error: Player {player_name} not found on team.")
            continue

        if keyword == "report":
            if len(parts) != 2:
                print("Error: Invalid command.")
                continue
            team_name = parts[1]
            team = league.get(team_name)
            if team is None:
                print("Error: Team not found.")
                continue
            print(team.get_report())
            continue

        print("Error: Invalid command.")
