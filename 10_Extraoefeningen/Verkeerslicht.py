class Verkeerslicht:

    def __init__(self, kleur = "rood"):
        self.kleur = kleur

    def __str__(self):
        return self.kleur

    def __repr__(self):
        return f"Verkeerslicht('{self.kleur}')"

    def volgende(self):
        if self.kleur == 'rood':
            self.kleur = 'groen'
        elif self.kleur == 'groen':
            self.kleur = 'oranje'
        else:
            self.kleur = 'rood'

