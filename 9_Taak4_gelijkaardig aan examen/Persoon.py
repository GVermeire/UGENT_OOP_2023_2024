from datetime import date

class Persoon:

    def __init__(self, naam, voornaam, woonplaats, jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum):
       self.naam = naam
       self.voornaam = voornaam
       self.woonplaats = woonplaats
       self.geboorte_datum = date(jaar_geboorte_datum,maand_geboorte_datum,dag_geboorte_datum)

    def get_naam(self):
        return self.naam

    def get_voornaam(self):
        return self.voornaam

    def get_woonplaats(self):
        return self.woonplaats

    def get_geboorte_datum(self):
        return self.geboorte_datum

    def set_voornaam(self, new_voornaam):
        self.voornaam = new_voornaam

    def set_woonplaats(self, new_woonplaats):
        self.woonplaats = new_woonplaats

    def is_ouder_dan(self, other_person):
        return self.geboorte_datum < other_person.get_geboorte_datum()

    def is_jonger_dan(self,other_person):
        return self.geboorte_datum > other_person.get_geboorte_datum()

    def wonen_in_zelfde_stad(self,other_person):
        return self.woonplaats == other_person.get_woonplaats()