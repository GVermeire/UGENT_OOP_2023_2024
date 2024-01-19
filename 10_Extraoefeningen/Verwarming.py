class Verwarming:

    def __init__(self, naam:str, temperatuur = 10.0, minimum = 0.0, maximum = 100.0):
        self.naam = naam
        self.toonTemperatuur = temperatuur
        self.minimum = minimum
        self.maximum = maximum


    def wijzig_temperatuur(self, n) -> float:
        self.toonTemperatuur += n
        if self.toonTemperatuur < self.minimum:
            self.toonTemperatuur = self.minimum
        elif self.toonTemperatuur > self.maximum:
            self.toonTemperatuur = self.maximum

    def temperatuur(self):
        return float(f'{self.toonTemperatuur:.1f}') #HIERAAN HEB IK EEN HALFUUR VERSPILT HIJ BLEEF '26.0' TONEN OP DODONA IPV 26.0 ZONDER HAAKJES, IN PYHTON WERKT HET WEL
    # IK heb deze lijn hierboven al op verschillende manieren proberen oplossen:
    # return f'{self.toonTemperatuur:.1f}' ma werkt GWN NIET, round werkt ook nie want die laat geen cijfer na de komma, geen formatering gebruiken en enkel return self... schrijven werkt ook nie ...
    # Oplossing gevonden dankzij PJ: gewoon een simpele 'float' ervoor zetten zoals het er nu staat. Die '.1f' is dus eig onnodig en heel veel hieronder is ook onnodig nu.
    
    def __str__(self):
        return f'{self.naam}: huidige temperatuur: {self.toonTemperatuur:.1f}; toegelaten min: {self.minimum:.1f}; toegelaten max: {self.maximum:.1f}'

    def __repr__(self):
        return f'Verwarming(\'{self.naam}\', {self.toonTemperatuur:.1f}, {self.minimum:.1f}, {self.maximum:.1f})'

# testen
kachel = Verwarming('kachel', 10, 20 , 90)
print(kachel)
