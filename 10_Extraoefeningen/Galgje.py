class Galgje:

    def __init__(self, woord, beurten = 6):
        self.woord = woord
        self.beurten = beurten
        self.letters = len(self.woord)

    def raadLetter(self, x):
        if x in self.woord:
            print(f'Correct: letter {x} komt voor in het woord.')
        else:
            self.beurten -= 1
            print(f'Fout: letter {x} komt niet voor in het woord.\nJe hebt nog {self.beurten} beurten.')

    def __str__(self):
        return f'Je hebt nog {self.beurten} beurten.\n......'
