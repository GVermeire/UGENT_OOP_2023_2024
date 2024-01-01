# https://youtu.be/XJaeYUOT2J4?si=5WJVsZj6Vm-XynBV
# https://youtu.be/RSl87lqOXDE?si=L_7t2mkx24whQtjo

from SoccerPlayer import SoccerPlayer

class SoccerTeam:
    def __init__(self, name:str): #dit toont hoe je kan zeggen welke soort van invoer name moet zijn
        self.name = name
        self.team = []

    def __str__(self):
        return f'Team name: {self.name}, players in team: {self.get_players()}'

    def add_player(self, player: SoccerPlayer) -> bool:
        self.team.append(player)
        return player in self.team

    def get_average_age(self) -> float:
        aantal_spelers = 0
        totaal = 0
        for i in self.team:
            totaal += SoccerPlayer.get_age(i)
            aantal_spelers += 1
        return totaal / aantal_spelers

    #def get_formation(self) -> str:
    #def get_name(self) -> str:

    def get_players(self) -> list:
        print(f'{self.team}')

    #def get_players_at(self, position: SoccerPlayer.position) -> list:

   # def substitute(self, player_out: SoccerPlayer, player_in: SoccerPlayer) -> bool:

#testen
team1 = SoccerTeam('De Rode Duivels')
print(team1)
speler_01 = SoccerPlayer("Karel", "de Grote", 28, SoccerPlayer.position.DF)
print(speler_01)
print(team1.add_player(speler_01))
print(team1) # status testen van wa er nu wel al werkt en wa nog nie


