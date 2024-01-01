from SoccerPlayer import SoccerPlayer  # Zorg ervoor dat de SoccerPlayer-klasse beschikbaar is in dezelfde map

class SoccerTeam:
    def __init__(self, name: str):
        self.name = name
        self.team = []

    def add_player(self, player: SoccerPlayer) -> bool:
        if len(self.team) < 11 and player not in self.team:
            self.team.append(player)
            return True
        return False

    def get_average_age(self) -> float:
        if not self.team:
            return 0.0
        total_age = sum(player.get_age() for player in self.team)
        return total_age / len(self.team)

    def get_formation(self) -> str:
        positions = [player.get_position() for player in self.team]
        formation = f"{positions.count('DF')}-{positions.count('MF')}-{positions.count('FW')}"
        return formation

    def get_name(self) -> str:
        return self.name

    def get_players(self) -> list:
        return self.team

    def get_players_at(self, position: SoccerPlayer.position) -> list:
        return [player for player in self.team if player.get_position() == position]

    def substitute(self, player_out: SoccerPlayer, player_in: SoccerPlayer) -> bool:
        if player_out in self.team and player_in not in self.team:
            if player_out.get_position() == 'GK':
                return False  # Kan geen doelman wisselen voor een veldspeler
            elif player_in.get_position() == 'GK':
                return False  # Kan geen veldspeler wisselen voor een doelman
            else:
                self.team.remove(player_out)
                self.team.append(player_in)
                return True
        return False

# Voorbeeld van lokaal testen
team1 = SoccerTeam('De Rode Duivels')
print(team1)
speler_01 = SoccerPlayer("Karel", "de Grote", 28, SoccerPlayer.position.DF)
print(speler_01)



