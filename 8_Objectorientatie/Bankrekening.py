class BankRekening: #class definition

    def __init__(self, rekeninghouder, rekeningnummer, bedrag=0): #Constructor (__init__ method):
        self.rekeninghouder = rekeninghouder
        self.rekeningnummer = rekeningnummer
        self.bedrag = bedrag

    def storten(self, n): # storten methode
        self.bedrag += n

    def afhalen(self, n): #afhalen method
        self.bedrag -= n

    def __str__(self):
        return f'{self.rekeninghouder}, {self.rekeningnummer}, bedrag: {self.bedrag}'

    def __repr__(self):
        return f"BankRekening('{self.rekeninghouder}', '{self.rekeningnummer}', {self.bedrag})"

# gebruiken van de klasse
Rekening = BankRekening("Gianni", "BE200000000", 100000)
Rekening.storten(4000)
Rekening.afhalen(2000)
print(Rekening) # hier kun je een kijken of het werkt en of je dus idd gwn die methodes kan gebruiken om aanpassen te brengen aan je bankrekening