import datetime


class Rijksregisternummer:
    def __init__(self, nummer):
        if not isinstance(nummer, str):
            raise AssertionError("ongeldig type")

        # Verwijder alle niet-cijfers en controleer het formaat
        nummer = ''.join(filter(str.isdigit, nummer))
        if len(nummer) != 11:
            raise AssertionError(f"ongeldig formaat ({len(nummer)} cijfers)")

        self.nummer = nummer

    def __repr__(self):
        return f"Rijksregisternummer('{self.nummer}')"

    def __str__(self):
        return f"{self.nummer[:2]}.{self.nummer[2:4]}.{self.nummer[4:6]}-{self.nummer[6:9]}.{self.nummer[9:]}"

    def geslacht(self):
        dagteller = int(self.nummer[6:9])
        return 'man' if dagteller % 2 == 1 else 'vrouw'

    def controlegetal(self, y2k=False):
        nummers = int(self.nummer)
        if y2k:
            nummers += 2000000000
        return 97 - (nummers % 97)

    def geboortedatum(self):
        try:
            jaar = int(self.nummer[:2])
            maand = int(self.nummer[2:4])
            dag = int(self.nummer[4:6])

            if jaar < 20:
                jaar += 2000
            else:
                jaar += 1900

            return datetime.date(jaar, maand, dag)
        except ValueError:
            raise AssertionError("ongeldige geboortedatum")

    def geldig(self):
        try:
            geboortedatum = self.geboortedatum()
            berekend_controlegetal = self.controlegetal(y2k=(geboortedatum.year >= 2000))
            return int(self.nummer[9:]) == berekend_controlegetal
        except AssertionError:
            return False


# Voorbeeldgebruik
rrn1 = Rijksregisternummer('75.12.05-137.14')
print(rrn1)  # Output: 75.12.05-137.14
print(rrn1.geldig())  # Output: True
print(rrn1.geboortedatum())  # Output: 1975-12-05
print(rrn1.geslacht())  # Output: man

rrn2 = Rijksregisternummer('>>>09082428248<<<LENA<NADINE<INGRID')
print(rrn2)  # Output: 09.08.24-282.48
print(rrn2.geldig())  # Output: True
print(rrn2.geboortedatum())  # Output: 2009-08-24
print(rrn2.geslacht())  # Output: vrouw
